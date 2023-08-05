import click
import json
import sys
import traceback

from lhub_extractors import util, params
from lhub_extractors import feature_extractor


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

def run_extractor(entrypoint_fn):
    global node_metadata
    global node_output_table

    type_mapper = get_input_converter(entrypoint_fn)

    for row in node_output_table:
        try:

            def coerce(column):
                try:
                    return type_mapper[column](row, column)
                except ValueError as ex:
                    util.print_error(
                        f"Invalid value for column {column}: [[{ex}}]", data=row
                    )
                    raise EndOfLoop()

            for column, column_data in row.items():
                mapped_column_data = coerce(column)
                row[column] = mapped_column_data

            result = entrypoint_fn(node_metadata, node_output_table)

            if result:
                util.print_result(json.dumps(result))
        except Exception:
            util.print_error(traceback.format_exc(), data=as_dict)

# expects a list of feature_extractors to execute
def run_extractors(entrypoints):
    for entry in entrypoints.split(","):
        entrypoint_fn = feature_extractor.all().get(entry).function
        run_extractor(entrypoint_fn)

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