from math import *
from typing import Union
from inspect import cleandoc

class Polygon:
    """This class creates a Polygon with the provided number of vertices and circumradius
    Args:
        _num_vertices : Number of Vertices for the Polygon to be created.
        _circumradius : The Circumradius for the Polygon to be created
    """

    def __init__(self, num_vertices: int = None, circumradius: Union[int, float] = None):
        self.num_vertices = num_vertices
        self.circumradius = circumradius

    @property
    def num_vertices(self) -> int:
        return self._num_vertices

    @property
    def circumradius(self) -> Union[int, float]:
        return self._circumradius

    @property
    def interior_angle(self) -> float:
        self._interior_angle = (self.num_vertices - 2) * (180 / self.num_vertices)
        return self._interior_angle

    @property
    def edge_length(self) -> float:
        self._edge_length = (2 * self.circumradius) * sin(pi / self.num_vertices)
        return self._edge_length

    @property
    def apothem(self) -> float:
        self._apothem = self.circumradius * cos(pi / self.num_vertices)
        return self._apothem

    @property
    def area(self) -> float:
        self._area = 0.5 * self.num_vertices * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self) -> float:
        self._perimeter = self.num_vertices * self.edge_length
        return self._perimeter

    @num_vertices.setter
    def num_vertices(self, new_num_vertices: int):
        assert new_num_vertices is not None, AttributeError("Number of vertices has to be provided")
        assert isinstance(new_num_vertices, int), ValueError("Number of vertices has to be integer.")
        assert new_num_vertices > 2, ValueError("Number of vertices cannot be less than 2.")
        self._num_vertices = new_num_vertices

    @circumradius.setter
    def circumradius(self, new_circumradius: Union[int, float]):
        assert new_circumradius is not None, AttributeError("Circumradius has to be provided")
        assert new_circumradius > 0, ValueError("Circumradius cannot be negative.")
        self._circumradius = new_circumradius

    @interior_angle.setter
    def interior_angle(self, new_interior_angle):        
        raise ValueError("Cannot set the value of interior angle of the polygon. It is auto-generated based upon the values of number of vertices and circumradius.")

    @edge_length.setter
    def edge_length(self, new_edge_length):
        raise ValueError("Cannot set the value of edge length of the polygon. It is auto-generated based upon the values of number of vertices and circumradius.")

    @apothem.setter
    def apothem(self, new_apothem):
        raise ValueError("Cannot set the value of apothem of the polygon. It is auto-generated based upon the values of number of vertices and circumradius.")

    @area.setter
    def area(self, new_area):
        raise ValueError("Cannot set the value of area of the polygon. It is auto-generated based upon the values of number of vertices and circumradius.")

    @perimeter.setter
    def perimeter(self, new_perimeter):
        raise ValueError("Cannot set the value of perimeter of the polygon. It is auto-generated based upon the values of number of vertices and circumradius.")


    def __str__(self) -> str:
        return cleandoc(\
            f"""
                --------------------------------------------------------
                \033[1mClass :\033[0m {self.__class__.__name__}
                \033[4mNumber of Vertices\033[0m : {self.num_vertices}
                \033[4mCircumradius\033[0m : {self.circumradius}
                \033[4mInterior Angle\033[0m : {self.interior_angle:.2f}
                \033[4mEdge Length\033[0m : {self.edge_length:.2f}
                \033[4mApothem\033[0m : {self.apothem:.2f}
                \033[4mArea\033[0m : {self.area:.2f}
                \033[4mPerimeter\033[0m : {self.perimeter:.2f}
                --------------------------------------------------------
            """)

    def __repr__(self) -> str:
        return f"Polygon(num_vertices = {self.num_vertices}, circumradius = {self.circumradius})"

    def __eq__(self, o: object) -> bool:
        assert isinstance(o, self.__class__), TypeError("Cannot compare classes of different types")
        assert hasattr(o, "num_vertices") and hasattr(o, "circumradius"), AttributeError("Classes to be compared has to have the attributes 'num_vertices' and 'circumradius'")
        if self.num_vertices ==  o.num_vertices and self.circumradius == o.circumradius:
            return True
        return False

    def __gt__(self, o: object) -> bool:
        assert isinstance(o, self.__class__), TypeError("Cannot compare classes of different types")
        assert hasattr(o, "num_vertices"), AttributeError("Classes to be compared has to have the attribute 'num_vertices'")
        if self.num_vertices > o.num_vertices :
            return True
        return False



    

    

    

