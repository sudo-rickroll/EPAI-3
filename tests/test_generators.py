from typing import Generator, Iterator
import io
import sys
from iterators import cars_iter, violations_made 

cars_obj = cars(r"C:\Users\Ranga\OneDrive\Desktop\nyc_parking_tickets_extract-1.csv")
def test_return_type():        
    assert isinstance(cars_obj, (Iterator, Generator)), TypeError("Object must be an iterator")

def test_violations_count():
    capturedOutput = io.StringIO()          
    sys.stdout = capturedOutput                   
    violations_made(cars_obj, "NISSA")                                 
    sys.stdout = sys.__stdout__                   
    assert "59" in capturedOutput.getvalue(), Exception("Wrong count of car model violations")