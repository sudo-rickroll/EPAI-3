from datetime import date
from dateutil import parser
from typing import Generator
from collections import namedtuple, Counter
from iterators import date_parser
import builtins


def csv_iter(entity_name, file_loc: str, *args) -> Generator:    
    with open(file_loc, encoding='utf8', errors='ignore') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        fields = next(rows)
        locals()[entity_name] = namedtuple(entity_name, fields)
        for row in rows:
            yield locals()[entity_name](*[getattr(builtins, data_type)(value) if hasattr(builtins, data_type) else locals()[data_type](value) for data_type, value in zip(args, row)])
