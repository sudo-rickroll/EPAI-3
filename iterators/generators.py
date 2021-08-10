from datetime import date
from dateutil import parser
from typing import Generator
from collections import namedtuple, Counter

def date_parser(date_obj: object) -> date:
    return parser.parse(date_obj).date()

def cars_iter(file_loc: str) -> Generator:
    with open(file_loc, encoding='utf8', errors='ignore') as f:
        fields = next(f)
        Cars = namedtuple("Cars", fields.replace(" ", ""))
        types = [int, str, str, str, date_parser, int, str, str, str]
        for row in f:
            yield Cars(*[data_type(value) for data_type, value in zip(types, row.strip("\n").split(","))])

def violations_count(cars_obj: object, *models):
    counter = Counter(item.VehicleMake.lower() for item in sorted(cars_obj, key=lambda x : x.VehicleMake) if item.ViolationDescription != "")
    for model in models:
        print(f"{model} : {counter[model.lower()]}") if model.lower() in counter else print("Model not present in CSV file.")


    
