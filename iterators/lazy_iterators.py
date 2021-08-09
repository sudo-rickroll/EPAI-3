import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    def __getattr__(self, name):
        if name == "count_vertices":
            count_vertices =  self._n
            setattr(self, name, count_vertices)
            return count_vertices
        elif name == "count_edges":
            count_edges =  self._n
            setattr(self, name, count_edges)
            return count_edges
        elif name == "circumradius":
            circumradius =  self._R
            setattr(self, name, circumradius)
            return circumradius
        elif name == "interior_angle":
            interior_angle =  (self._n - 2) * 180 / self._n
            setattr(self, name, interior_angle)
            return interior_angle
        elif name == "side_length":
            side_length =  2 * self._R * math.sin(math.pi / self._n)
            setattr(self, name, side_length)
            return side_length
        elif name == "apothem":
            apothem =  self._R * math.cos(math.pi / self._n)
            setattr(self, name, apothem)
            return apothem
        elif name == "area":
            area =  self._n / 2 * self.side_length * self.apothem
            setattr(self, name, area)
            return area
        elif name == "perimeter":
            perimeter =  self._n * self.side_length
            setattr(self, name, perimeter)
            return perimeter
        else:
            raise AttributeError(f"{self} has no attribute named '{name}'") 
    
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R      
    
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    

    def __iter__(self):
        return self.Polygon_Iterator(self._m, self._R)    
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]

    class Polygon_Iterator:
        def __init__(self, m, R):
            self._m = m
            self._R = R
            self._i = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self._i > self._m:
                raise StopIteration
            else:
                polygon = Polygon(self._i, self._R)
                self._i += 1
                return polygon


