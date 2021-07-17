Name : `Rangasai K R`</br>
Email ID : `sai.ranga3@gmail.com`

# Decorators

This repository contains the functions illustrating the use of Decorators and Decorator Factories.

A Decorator function is a function enclosing an inner function that runs the main function that is to be decorated, along with the additional processes that need to be carried out while running the main function. It takes the main function that is to be run, as an argument and returns a callable which runs the main function along with the additional processes specified, when called.

Example: 
```
def decorator (fn):
    def inner (*args, **kwargs):
        """main_function and additional functions are run here"""
        pass
    return inner

@decorator
def main_function (*args, **kwargs):
    pass

```

A Decorator Factory is a function that encloses the Decorator function that is used to pass arguments to the decorator in the Pie Syntax.

The following functions have been written to illustrate the usage of decorators and decorator functions:


### odd_it

This Decorator function allows to run a function only at odd seconds, else prints out "We're even!". The <i>odd_it</i> function takes in the main function as the function argument. Inside this function, there is an <i>inner</i> function that takes in the arguments that are to be passed to the main function. It checks whether the current time at which the program is executed contains odd seconds. If so, it executes the main function. Otherwise, it returns the string "We're even!"


### logger

This Decorator function logs the time at which the function is called, the description (docstring) of the called function and the annotations of the function. Here, we import the required modules inside the decorator function so as to not overload the memory with modules that are not required in other places. We use `@wraps(fn)` so as to override the function attributes of the inner function with the gunction attributes of the main function, so that they are not lost while decorating. Hence, the main function attributes are still preserved and are accessible.


### decorator_factory

This Decorator factory function provides access to variables based upon the access level type passed as input to the decorator factory function. Here, we pass an access level token as string to the decorator factory. Inside the decorator function named <i>outer</i>, we initialize four free variables for use inside the closure. These variables are then returned based upon the access level token provided.


### authenticate

This Decorator Factory function runs the function inside it only if the password that is passed as an input to the actual function is the same as the password that is set through the input to the decorator function. Here, we pass a string to the decorator and we set this string as the password. When calling the function, the argument of the function is matched with the argument of this parameterised decorator and the function is run if the password matches. Else, "Wrong Password" is returned as output.


### timed(reps)

This decorator function takes an input to it that specifies the amount of times a function is run. It then runs the actual function that many number of times and calculates the overall time taken over all the iterations and also the average time taken for each iteration of the function to run.
