from datetime import date
from dateutil import parser
from typing import Generator
from collections import namedtuple, Counter
from contextlib import contextmanager
from iterators import date_parser
import builtins

@contextmanager
def csv_iter(entity_name, file_loc: str, *args) -> Generator:
    try:
        with open(file_loc, encoding='utf8', errors='ignore') as f:
            rows = csv.reader(f, delimiter=',', quotechar='"')
            fields = next(rows)
            locals()[entity_name] = namedtuple(entity_name, fields)
            for row in rows:
                yield locals()[entity_name](*[getattr(builtins, data_type)(value) for data_type, value in zip(args, row) if data_type in builtins else locals()[data_type](value)])

    finally:
        del locals()[entity_name]
