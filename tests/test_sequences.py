from sequences import Polygon
import pytest
import re

polygon_inputs = [(-1, -1), (5, -1), (2.5, 0) ,(None,), (4,)]
regex_matches = [r".*vertices.*less.* than (2|two)", r".*circumradius.*(negative|less.* than (0|zero))", r".* vertices.*integer", r".*vertices.*provided.*", r".*circumradius.*provided"]

@pytest.mark.parametrize('input', zip(polygon_inputs, regex_matches))
def test_class_inputs(input):
    with pytest.raises(Exception) as execinfo:
        polygon_object = Polygon(*input[0])

    assert isinstance(execinfo.value.args[0], ValueError) or isinstance(execinfo.value.args[0], AttributeError) and re.compile(input[1]).match(execinfo.value.args[0].args[0].lower()) is not None
    
polygon_properties = ["interior_angle", "edge_length", "apothem", "area", "perimeter"]
polygon_object = Polygon(4,5)

@pytest.mark.parametrize('property', polygon_properties)
def test_class_properties(property):
    with pytest.raises(Exception) as execinfo:
        setattr(polygon_object, property, 0)
    
    assert isinstance(execinfo.value, ValueError) and re.compile(r".*cannot.*set.*value").match(execinfo.value.args[0].lower()) is not None
    
def test_eq_types():
    obj = 4
    with pytest.raises(Exception) as execinfo:
        polygon_object == obj

    assert isinstance(execinfo.value.args[0], TypeError) and re.compile(r".*classes.*different types.*").match(execinfo.value.args[0].args[0].lower()) is not None

def test_gt_types():
    obj = 4
    with pytest.raises(Exception) as execinfo:
        polygon_object > obj

    assert isinstance(execinfo.value.args[0], TypeError) and re.compile(r".*classes.*different types.*").match(execinfo.value.args[0].args[0].lower()) is not None





    
