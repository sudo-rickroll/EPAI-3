from typing import Generator
from collections import namedtuple
from iterators import date_parser
import builtins
import csv

def combine_namedtuples(combined_namedtuple_name, *args, **kwargs):
    file_locs = args
    entities = list(kwargs.keys())
    data_types = list(kwargs.values())
    namedtuple_iters, namedtuple_fields = [], []
    for file_loc, entity, data_type in zip(file_locs, entities, data_types):
        namedtuple_iters.append(csv_iter(file_loc, entity, namedtuple_fields, *data_type))
    for i, j, k, l in zip(*[namedtuple_iters[r] for r in range(0, len(namedtuple_iters))]):
        if not hasattr(locals(), combined_namedtuple_name):
            locals()[combined_namedtuple_name] = namedtuple(combined_namedtuple_name, namedtuple_fields)
            yield locals()[combined_namedtuple_name](*list(dict.fromkeys(i + j + k + l)))


def csv_iter(file_loc, entity_name, namedtuple_fields=None, *args) -> Generator:
    with open(file_loc, encoding='utf8', errors='ignore') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        fields = next(rows)
        if namedtuple_fields is not None:
            namedtuple_fields.extend([field for field in fields if field not in namedtuple_fields])
        locals()[entity_name] = namedtuple(entity_name, fields)
        for row in rows:
            yield locals()[entity_name](*[getattr(builtins, data_type)(value) if hasattr(builtins, data_type) else globals()[data_type](value) for data_type, value in zip(args, row)])

def stale_records(sequence, column):
    yield from filter(lambda x : getattr(x, column) > date(2017, 3, 1), sequence)

def highest_count(iterator_obj, *args):
    counter = Counter([tuple(getattr(item, arg) for arg in args) for item in iterator_obj])
    counter_male = sorted([(k[1],v) for k, v in counter.items() if k[0].lower() == 'male'], key = lambda x : x[1], reverse=True)
    counter_male = [i for i in counter_male if i[1] == counter_male[0][1]]
    counter_female = sorted([(k[1],v) for k, v in counter.items() if k[0].lower() == 'female'], key = lambda x : x[1], reverse=True)
    counter_female = [i for i in counter_female if i[1] == counter_female[0][1]]
    return counter_male, counter_female
