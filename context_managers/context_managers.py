from typing import Generator
from collections import namedtuple
from iterators import date_parser
import builtins
import csv

# Decorator factory to combine namedtuples across multiple iterators (currently set to combine namedtuples across 4 iterators but can be made dynamic with a small change)
def combine_namedtuples(combined_namedtuple_name, *args, **kwargs):
    file_locs = args
    entities = list(kwargs.keys())
    data_types = list(kwargs.values())
    def decorator(fn):
        namedtuple_iters, namedtuple_fields = [], []
        from functools import wraps
        @wraps(fn)
        def inner(*args, **kwargs):
            nonlocal namedtuple_fields
            for file_loc, entity, data_type in zip(file_locs, entities, data_types):
                namedtuple_iters.append(fn(file_loc, entity, namedtuple_fields, *data_type))
            for i, j, k, l in zip(*[namedtuple_iters[r] for r in range(0, len(namedtuple_iters))]):
                if not hasattr(locals(), combined_namedtuple_name):
                    locals()[combined_namedtuple_name] = namedtuple(combined_namedtuple_name, namedtuple_fields)
                yield locals()[combined_namedtuple_name](*list(dict.fromkeys(i + j + k + l)))
        return inner
    return decorator

# Function to create iterator containing namedtuple records from a csv
def csv_iter(file_loc, entity_name, namedtuple_fields=None, *args) -> Generator:
    with open(file_loc, encoding='utf8', errors='ignore') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        fields = next(rows)
        if namedtuple_fields is not None:
            namedtuple_fields.extend([field for field in fields if field not in namedtuple_fields])
        locals()[entity_name] = namedtuple(entity_name, fields)
        for row in rows:
            yield locals()[entity_name](*[getattr(builtins, data_type)(value) if hasattr(builtins, data_type) else globals()[data_type](value) for data_type, value in zip(args, row)])
