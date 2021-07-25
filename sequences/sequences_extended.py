from sequences import Polygon
from typing import Iterable, Union
from collections.abc import Sequence
from sequences import Polygon

class Polygon_Sequence:

    """This class takes in the number of vertices for largest polygon in the sequence and a common circumradius for all the polygons and creates sequences of polygons starting with 3 vertices and the provided circumradius
    Args:
        num_vertices_largest : Number of vertices for the Polygon with the most number of vertices in the sequence
        circumradius : Common circumradius for all the polygons
    """

    def __init__(self, num_vertices_largest: int, circumradius: Union[int, float]) -> None:
        self.num_vertices_largest = num_vertices_largest
        self.circumradius = circumradius
        self._index = 0

    @property
    def num_vertices_largest(self) -> int:
        return self._num_vertices_largest

    @property
    def circumradius(self) -> Union[int, float]:
        return self._circumradius

    @property
    def polygons(self) -> list[Polygon]:
        self._polygons = [Polygon(num_vertices, self.circumradius) for num_vertices in range(3, self.num_vertices_largest + 1)]
        return self._polygons

    @property
    def max_efficiency(self) -> float:
        self._max_efficiency = float(f"{max([polygon.area / polygon.perimeter for polygon in self.polygons]) : .2f}")
        return self._max_efficiency

    @num_vertices_largest.setter
    def num_vertices_largest(self, new_num_vertices_largest: int) -> None:
        self._num_vertices_largest = new_num_vertices_largest

    @circumradius.setter
    def circumradius(self, new_circumradius: Union[int, float]) -> None:
        self._circumradius = new_circumradius

    @polygons.setter
    def polygons(self, new_polygons: Sequence[Polygon]) -> None:
        raise ValueError("Cannot set the polygon objects. It is auto-generated based upon the number of vertices and circumradius provided.")

    @max_efficiency.setter
    def max_efficiency(self, new_max_efficiency : Union[int, float]) -> None:
        raise ValueError("Cannot set the value of max efficiency of the polygons. It is auto-generated based upon the highest area to perimeter ratio among the sequence of polygons.")

    def __len__(self) -> int:
        return self.num_vertices_largest - 2

    def __iter__(self):
        return self

    def __next__(self) -> Union[Polygon, StopIteration]:
        if self._index == len(self.polygons):
            self._index = 0
            raise StopIteration
        else:
            self._index += 1
            return self.polygons[self._index - 1]

    def __getitem__(self, index: Union[int, slice]) -> Polygon:
        return self.polygons[index]
            
    def __repr__(self) -> str:
        return f"Polygon_Sequence(num_vertices_largest = {self.num_vertices_largest}, circumradius = {self.circumradius})"

    def __str__(self) -> str:
        return '\n'.join(list(map(str, self.polygons)))






    

    

    

    

    

    

    
