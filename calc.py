# Unit Testing Sample

""" Addition Function"""
def add (x, y):
	return x + y

""" Subtration Function """
def subtract (x, y):
	return x - y

""" Multiplication Function """
def multiply (x , y):
	return x * y

""" Division """
def divide (x, y):
	if y == 0:
		raise ValueError("Can not divide by zero!")
	return x / y