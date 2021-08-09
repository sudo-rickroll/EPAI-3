# Iterators

This directory contains the file named <b>iterators.py</b>, which implements a non-exhaustible iterator from the "Polygon_Sequence" class from <a href="https://github.com/sudo-rickroll/Python-Scratchpad/tree/main/sequences">this</a> directory.

It also contains a file named <b>lazy_iterators.py</b> which contains a class that modifies the code <a href="https://github.com/sudo-rickroll/Python-Scratchpad/blob/main/sequences/sequences.py">here</a> such that the attributes computed are lazy attributes (computed only once) and another class that modifies the code <a href="https://github.com/sudo-rickroll/Python-Scratchpad/blob/main/sequences/sequences_extended.py">here</a> such that the list is converted to a lazy iterator that is computed only when called.

The test files are placed in the <i>/tests</i> directory and are named named <b>test_iterators</b> and <b>test_lazy_iterators</b> respectively.
