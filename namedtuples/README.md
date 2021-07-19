# Named Tuples

This directory contains the modules for namedtuples. Faker library has been made use of and comparisons between namedtuple and dict has been made inside the code. The main file <b>namedtuple.py</b> consists of the code to load a specified number of profiles from faker library and calculate things like most common blood group, average age, oldest person's age and average location coordinates of the profiles. These profiles are also loaded inside a dictionary and the same calculations that are made inside namedtuples are also made here to compare the speed of operation between namedtuples and dictionaries.

The test file for the module in this directory exists in <i>/tests/</i> folder with the name <b>test_namedtuple.py</b>, which is used as a test file for the main module and is run with pytest by Github Actions.
