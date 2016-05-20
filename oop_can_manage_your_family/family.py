class Person():

	'''
	Other Classes Referenced
	'''

	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]


	'''
	Constructor
	'''
	__init__(self, id, first_name, date_of_birth. genre, eyes_color)
	if id < 0 or type(id) is not int:
		raise Exception("id is not an integer")
	if eyes_color not in Person.EYES_COLORS or type(eyes_color) is not str:
		raise Exception("Your eyes_color is not kosher")



	'''
	Classes
	'''

	'''
	Private Attributes
	'''

	'''
	Public Attributes
	'''

	'''
	Public Methods
	'''
