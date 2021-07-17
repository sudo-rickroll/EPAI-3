from functools import wraps
from datetime import datetime
from time import perf_counter



def odd_it(fn: function) -> function:
	"""This Decorator function allows to run a function only at odd seconds, else prints out "We're even!"""
	def inner(*args, **kwargs) -> function:
		if datetime.now().second % 2 == 1:
			return fn(*args, **kwargs)
		print("We're even!")
	return inner

def logger(fn: function) -> function:
	"""This Decorator function logs the time at which the function is called, the description (docstring) of the called function and the annotations of the function."""
	import datetime, inspect	
	@wraps(fn)
	def inner(*args, **kwargs) -> function:
		print(f"Function Name {fn.__name__} was called at {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5.5)))}")
		print(f"Function description : {fn.__doc__}")
		print(f"Function annotation : {inspect.signature(fn)}")
		start = perf_counter()
		func_obj = fn(*args, **kwargs)
		end = perf_counter()
		print("Execution time of function '{fn.__name__}' is {end - start}")
		return func_obj
	return inner


def decorator_factory(access: str) -> function:
	"""This Decorator factory function provides access to variables based upon the access level type passed as input to the decorator factory function."""
	def outer(fn: function) -> function: 
		var1, var2, var3, var4 = 0, 0, 0, 0
		@wraps(fn)
		def inner() -> function:
			if access == 'high':
				return [var1, var2, var3, var4]
			elif access == 'mid':
				return [var2, var3, var4]
			elif access == 'low':
				return [var3, var4]
			elif access == 'no':
				return [var4]
			else:
				return "Improper access keyword set"
		return inner
	return outer 



def authenticate(set_password: str) -> function:
	"""This Decorator function runs the function inside it only if the password that is passed as an input to the actual function is the same as the password that is set through the input to the decorator function."""
	def outer(fn: function) -> function:
		@wraps(fn)
		def inner(arg: str) -> function:
			if set_password == arg:
				return fn()
			else:
				return "Wrong Password"
		return inner
	return outer


# The timing function
def timed(reps: int) -> function:
	"""This decorator function takes an input to it that specifies the amount of times a function is run. It then runs the actual function that many number of times and calculates the overall time taken over all the iterations and also the average time taken for each iteration of the function to run."""
	def outer(fn: function) -> function:
		@wraps(fn)
		def inner(*args, **kwargs) -> function:
			end = 0
			for i in range(reps):
				start = perf_counter()
				result = fn(*args, **kwargs)
				end += perf_counter() - start
			print("Total Time Elapsed : ", end)
			print("Total times the function has been run : ", reps)
			print("Average Time Elapsed : ", end / reps)
			return result
		return inner
	return outer 


			

