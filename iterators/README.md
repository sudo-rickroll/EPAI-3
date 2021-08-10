# Iterators
This directory contains three main files - <b>iterators.py</b>, <b>lazy_iterators.py</b> and <b>generators.py</b>

<b>iterators.py</b> implements a non-exhaustible iterator from the "Polygon_Sequence" class from <a href="https://github.com/sudo-rickroll/Python-Scratchpad/tree/main/sequences">this</a> directory.

<b>lazy_iterators.py</b> contains a class that modifies the code <a href="https://github.com/sudo-rickroll/Python-Scratchpad/blob/main/sequences/sequences.py">here</a> such that the attributes computed are lazy attributes (computed only once) and another class that modifies the code <a href="https://github.com/sudo-rickroll/Python-Scratchpad/blob/main/sequences/sequences_extended.py">here</a> such that the list is converted to a lazy iterator that is computed only when called.

<b>generators.py</b> contains two functions that make use of <a href="https://github.com/sudo-rickroll/Python-Scratchpad/blob/main/resources/nyc_parking_tickets_extract.csv">this</a> CSV File. It has a function that loads the data from the csv file onto a lazy iterator (generator). The other function in this file calculates and displays the number of violations for vehicle model(s) that is entered as input to the function by the user.


The test files are placed in the <i>/tests</i> directory and are named <b>test_iterators</b>, <b>test_lazy_iterators</b> and <b>test_generators</b> respectively.
