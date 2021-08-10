from typing import Generator, Iterator
import io
import sys
from iterators import cars_iter, violations_count 

cars_obj = cars_iter(r"../resources/nyc_parking_tickets_extract.csv")

def test_return_type():        
    assert isinstance(cars_obj, (Iterator, Generator)), TypeError("Object must be an iterator")

def test_violations_count():
    capturedOutput = io.StringIO()          
    sys.stdout = capturedOutput                   
    violations_count(cars_obj, "NISSA")                                 
    sys.stdout = sys.__stdout__                   
    assert "59" in capturedOutput.getvalue(), Exception("Wrong count of car model violations")
