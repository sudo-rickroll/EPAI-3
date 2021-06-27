# Closures

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable
A. Function named <i>docstringcounter</i> is written with the threshold of the docstring to be compared as the optional argument (which is 50 in this case). It contains a closure inside, named <i>check_docstring</i> which takes a function as anrgument, whose doctring length is to be compared with the docstring_threshold. It will then output the length of the docstring of this argument function and also indicating whether this function's docstring is less than/more than/equal to the docstring_threshold.

2. Write a closure that gives you the next Fibonacci number
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries
