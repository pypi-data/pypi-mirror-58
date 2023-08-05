from docstring_parser import parse
from typing import Dict, Callable, Any

CONVERTIBLE_TYPES = [int, str, float, bool]
EXTRACTOR_TYPES = ["int", "str", "float", "bool"]

def to_convertible(extractor_type):
    if extractor_type == 'int':
        return int
    if extractor_type == 'str':
        return str
    if extractor_type == 'float':
        return float
    if extractor_type == 'bool':
        return bool

def convert(c):
    def do_convert(raw: Dict[str, Any], column):
        value = raw[column]
        if c in [str, float]:
            return c(value)
        if c == int:
            return int(float(value))
        elif c == bool:
            return DataType.BOOL.coerce(value)

    return do_convert

def get_input_converter(entrypoint_fn) -> Dict[str, Callable[[str], Any]]:
    docs = entrypoint_fn.__doc__
    parsed = parse(docs)

    converter = {}

    for param in parsed.params:
        if param.type_name is not None:
            column_name = param.arg_name
            type_name = param.type_name

            if type_name in EXTRACTOR_TYPES:
                converter[column_name] = convert(to_convertible(type_name))
