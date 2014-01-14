"""Recreating OOP without using data structures associated with OOP.

The essential data structures and language constructs required to recreate
OOP in this module are:

	pointers
	variables
	for loops
	functions
	arrays
	associative arrays

The following OOP constructs not used in this module are:
	
	Python classes

This implementation of OOP includes the following features:

	instantiation
	...

This implementation of OOP does not (yet) include:
	
	inheritance
	polymorphism
	encapsulation
	...
"""

def cls(attributes, methods):
	"""Define a new class.

	Arguments:
		attributes - a list of strings representing names of attributes
		methods - an associative array of strings representing method names
			mapped to function objects, which each require an instance of
			the class for its first parameter

	Returns:
		a class represented by {attributes, methods, instances},
		where "instances" is a list containing the data structures
		representing instances
	"""

	return {
		"attributes": attributes, 
		"methods": methods,
		"instances": []
	}

def inst(cls):
	"""Instantiate the given class.

	Returns:
		an instance represented by {_cls, attributes}, where "attributes"
		is an associative array of strings representing attribute names mapped
		to lists, which are initially empty, containing attribute values
	"""

	instance = {
		"class": cls, 
		"attributes": {attr: [] for attr in cls["attributes"]}
	}

	cls["instances"].append(instance)
	return instance

def geta(inst, a_name):
	"""Get the requested attribute from the given instance."""

	return inst["attributes"][a_name]

def seta(inst, a_name, value):
	"""Set the specified attribute of inst to value."""

	inst["attributes"][a_name] = value

def method(inst, m_name, args):
	"""Run the method specified by m_name with the given instance and
	arguments.

	Arguments:
		inst - an instance
		m_name - the name of the method to be called
		args - a list of arguments to call the method with
	"""

	args = args.extend([inst])
	result = apply(inst["class"]["methods"][m_name], args)
	return result

if __name__ == "__main__":
	pass