from iterators import Polygon_Sequence_Iterable

def test_iter_exhaustion():

    polygon_obj = Polygon_Sequence_Iterable(5,2)
    assert "__iter__" in dir(polygon_obj), "Iterable class must contain the __iter__ method to be converted to an iterator."
    
    iter_obj = iter(polygon_obj)    
    for i in iter_obj:
        pass

    assert next(iter_obj) is not None, "Iterator has to be non-exhaustible."
