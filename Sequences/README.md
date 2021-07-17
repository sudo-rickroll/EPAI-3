# Sequences

This directory consists of two main files - <b>sequences.py</b> and <b>sequences_extended.py</b>.

<ul>
  <li>The sequences.py file contains a Polygon class with some properties. It takes two properties (number of vertices and circumradius of the polygon) as input values and the rest of the properties (interior angle, edge length, apothem, area, perimeter) are automatically created.</li>
  <li>The sequences_extended.py module contains a Polygon_Extended class. It takes the maximum number of vertices and a common circumradius as input. Then it creates as many polygons, starting from the polygon that can be created with the least number of sides(3) till polygons that can be created with the maximum number of vertices as specified. All these polygons will have the common circumradius as specified. It will then calculate the max efficiency property by calculating the maximum of the efficiencies (ratio of area to perimeter) amongst the polygons.</li>
</ul>

</br>
It also contains two files for testing - <b>test_sequences.py</b> and <b>test_sequences_extended.py</b> which are the test files run with pytest inside github actions.
