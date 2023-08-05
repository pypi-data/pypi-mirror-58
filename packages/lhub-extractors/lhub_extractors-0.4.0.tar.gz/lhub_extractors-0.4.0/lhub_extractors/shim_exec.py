import click
import json
import sys
import traceback

from lhub_extractors import util, params
from lhub_extractors import feature_extractor
from dataclasses_json import dataclass_json
from dataclasses import dataclass
from typing import List

@dataclass
@dataclass_json
class FeatureExtractorExecutionResult:
    entrypoint: str
    result: str
    errors: List[str]

@dataclass
@dataclass_json
class FeatureExtractorExecutionResults:
    results: List[FeatureExtractorExecutionResult]
    errors: List[str]

node_metadata = {}
required_columns = {}
node_output_table = []

def read_input_data():
    global node_metadata
    global node_output_table

    as_dict_1 = json.loads(sys.stdin.readline())

    if 'node_metadata' in as_dict_1:
        node_metadata = as_dict_1['node_metadata']

    for data in sys.stdin.readlines():
        as_dict = json.loads(data)

        if 'row' in as_dict:
            row = as_dict['row']
            node_output_table.append(row)

def run_extractor(entrypoint, entrypoint_fn):
    global node_metadata
    global node_output_table

    type_mapper = params.get_input_converter(entrypoint_fn)
    column_to_type_map = params.get_input_type_map(entrypoint_fn)

    errors = []
    required_columns = list(column_to_type_map.keys())
    node_output_table_columns = node_metadata['columns']
    feature_extractor_node_output_table = []

    if required_columns <= node_output_table_columns:
        for row in node_output_table:
            try:
                def coerce(column, column_data):
                    try:
                        return type_mapper[column](row, column)
                    except ValueError:
                        errors.append(
                            f"Invalid value: {column_data} for column {column}. Expected data of type: {column_to_type_map[column]}"
                        )
                        raise EndOfLoop()

                mapped_row = {}
                for column, column_data in row.items():
                    if column in required_columns:
                        mapped_column_data = coerce(column, column_data)
                        mapped_row[column] = mapped_column_data
                feature_extractor_node_output_table.append(mapped_row)

            except EndOfLoop:
                break

            except Exception:
                error = json.dumps({
                 "error": traceback.format_exc(),
                 "data": row
                })
                errors.append(error)
                break
    else:
        errors.append(f"Required columns: {required_columns} did not exist in the node output table columns: {node_output_table_columns}")

    result = {}

    if not errors:
        try:
            result = entrypoint_fn(node_metadata, feature_extractor_node_output_table)
            if result:
                return FeatureExtractorExecutionResult(
                    entrypoint = entrypoint,
                    result = result,
                    errors = errors
                )
        except Exception:
            error = json.dumps({
                "error": traceback.format_exc(),
                "data": row
            })
            errors.append(error)

    return FeatureExtractorExecutionResult(
        entrypoint = entrypoint,
        result = result,
        errors = errors
    )

# expects a list of feature_extractors to execute
def run_extractors(entrypoints):
    results = []
    errors = []
    for entrypoint in entrypoints.split(","):
        try:
            entrypoint_fn = feature_extractor.all().get(entrypoint).function
            result = run_extractor(entrypoint, entrypoint_fn)
            results.append(result)
        except Exception as ex:
            errors.append(
                json.dumps({
                    "entrypoint": entrypoint,
                    "error": ex
                })
            )

    feature_extractor_results = FeatureExtractorExecutionResults(
        results = results,
        errors = errors
    )

    util.print_result(feature_extractor_results.to_json())

class EndOfLoop(Exception):
    pass

@click.command()
@click.option("--entrypoints", "-e", required=True)
def main(entrypoints):
    errors = util.import_workdir()
    if errors:
        util.hard_exit_from_instantiation(str(errors[0]))
    read_input_data()
    run_extractors(entrypoints)

if __name__ == "__main__":
    main()