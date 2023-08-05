from typing import List
from pathlib import Path

import json
import importlib

def import_workdir() -> List[str]:
    errors = []
    docstrings = []
    for file in Path(".").iterdir():
        if file.suffix == ".py":
            file_name = file.name[: -len(".py")]
            if "." in file_name:
                errors.append(f"Python files cannot contain dots: {as_module}")
                continue
            try:
                importlib.import_module(file_name)
            except Exception as ex:
                errors.append(ex)
    return errors

def print_result(msg):
    print(f"[result] {msg}")

def invalid_extractor(code, error):
    raise InvalidExtractor(code, error)

def deser_output(output: str):
    prefix = "[result]"
    processed = ""
    for line in output.splitlines():
        if line.startswith(prefix):
            processed += line[len(prefix) :]
    try:
        return json.loads(processed)
    except json.decoder.JSONDecodeError:
        raise Exception(f"Could not parse JSON: {output}")

def print_error(message: str, data=None):
    error = {"has_error": True, "error": message, "data": data}
    print_result(json.dumps(error))

class InvalidExtractor(Exception):
    def __init__(self, key, message):
        super().__init__(f"{message} [{key}]")
