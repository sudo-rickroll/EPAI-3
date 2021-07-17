from sequences_extended import Polygon_Sequence
import pytest

def test_sequences_properties():
    polygon = Polygon_Sequence(4, 4)
    assert len(polygon) == 2, "Length of Polygon_Sequence class has to be equal to the number of Polygons inside it."
    assert polygon[1].num_vertices == 4, "Largest Polygon in the sequence must have as many vertices as the num_vertices_largest parameter argument value in the Polygon_Sequence class."
    