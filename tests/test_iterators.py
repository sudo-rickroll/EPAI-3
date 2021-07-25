from iterators import Polygon_Sequence_Iterable

def test_iter_exhaustion():

    polygon_obj = Polygon_Sequence_Iterable(5,2)

    for i in polygon_obj:
        pass

    assert next(iter(polygon_obj)) is not None, "Iterator has to be non-exhaustible"