from sequences import Polygon_Sequence
from typing import Iterator, Union

class Polygon_Sequence_Iterable():
    """This class implements a non-exhaustive iterator for the class 'Polygon_Sequence'
    Args:
        num_vertices_largest : Number of vertices for the Polygon with the most number of vertices in the 'Polygon_Sequence' class
        circumradius : Common circumradius for all the polygons in the 'Polygon_Sequence' class
    """

    def __init__(self, num_vertices_largest: int, circumradius: Union[int, float]) -> None:
        self._num_vertices_largest = num_vertices_largest
        self._circumradius = circumradius    

    @property
    def num_vertices_largest(self) -> int:
        return self._num_vertices_largest

    @property
    def circumradius(self) -> Union[int, float]:
        return self._circumradius

    @num_vertices_largest.setter
    def num_vertices_largest(self, new_num_vertices_largest: int) -> None:
        self._num_vertices_largest = new_num_vertices_largest

    @circumradius.setter
    def circumradius(self, new_circumradius: Union[int, float]) -> None:
        self._circumradius = new_circumradius

    def __iter__(self) -> Iterator:
        return Polygon_Sequence(self.num_vertices_largest, self.circumradius)      


a = Polygon_Sequence_Iterable(5,2)

for i in a:
    pass

print(next(iter(a)) is not None)
