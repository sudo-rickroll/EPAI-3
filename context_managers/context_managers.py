from datetime import date
from iterators import date_parser
from typing import Generator, Iterator, Iterable, NamedTuple, List, Tuple, Union
from collections import namedtuple, Counter
import builtins
import csv


def combine_namedtuples(combined_namedtuple_name: str, *args, **kwargs) -> Iterator[NamedTuple]:
    """This function is used to combine the namedtuples present across multiple iterators.
    Args:
        combined_namedtuple_name : string to be used as the name of the newly created namedtuple generated by combining namedtuples from across different iterators.
        args : array of file locations to be used by the 'csv_iter' function to create the iterators of namedtuples that are to be combined.
        kwargs : dictionary containing the names of the different namedtuples inside the iterators as keys and the datatypes of fields inside them as string values to be used by the 'csv_iter' function.
    """
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


def csv_iter(file_loc: str, entity_name: str, namedtuple_fields: List[str]=None, *args) -> Iterator[NamedTuple]:
    """This function is used to read a CSV file and generate an iterator containing the namedtuples.
    Args:
        file_loc : location of the csv file to be parsed.
        entity_name : name for the namedtuples to be created.
        namedtuple_fields : optional list to be filled with the field names of the namedtuple to be created.
        args : list of datatypes for the fields in the namedtple.
    """
    with open(file_loc, encoding='utf8', errors='ignore') as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        fields = next(rows)
        if namedtuple_fields is not None:
            namedtuple_fields.extend([field for field in fields if field not in namedtuple_fields])
        locals()[entity_name] = namedtuple(entity_name, fields)
        for row in rows:
            yield locals()[entity_name](*[getattr(builtins, data_type)(value) if hasattr(builtins, data_type) else globals()[data_type](value) for data_type, value in zip(args, row)])

def stale_records(sequence: Union[Generator[NamedTuple,None,None], Iterator[NamedTuple], Iterable[NamedTuple]], column: str) -> Iterator[NamedTuple]:
    """This function generates stale records from an iterable/iterator based on a particular column and a condition for it.
    Args:
        sequence : Iterable/Iterator to fetch the records from.
        column : Column name in string. Must be a column of datetime type. 
    """
    yield from filter(lambda x : getattr(x, column) > date(2017, 3, 1), sequence)

def highest_count(sequence: Union[Generator[NamedTuple,None,None],Iterator[NamedTuple], Iterable[NamedTuple]], *args)-> Tuple[List[Tuple]]:
    """This function is used to generate an entity with the highest count based upon the gender column values inside it.
    Args:
        sequence : Iterable/Iterator to fetch the records from.
        args : List of column names for which the highest count needs to be obtained.

    """
    counter = Counter([tuple(getattr(item, arg) for arg in args) for item in sequence])
    counter_male = sorted([(k[1],v) for k, v in counter.items() if k[0].lower() == 'male'], key = lambda x : x[1], reverse=True)
    counter_male = [i for i in counter_male if i[1] == counter_male[0][1]]
    counter_female = sorted([(k[1],v) for k, v in counter.items() if k[0].lower() == 'female'], key = lambda x : x[1], reverse=True)
    counter_female = [i for i in counter_female if i[1] == counter_female[0][1]]
    return counter_male, counter_female