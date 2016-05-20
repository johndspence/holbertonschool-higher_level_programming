
''' Class '''
class Person():

	''' Other Classes Referenced'''
	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]

	'''Constructor'''
	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''Public Methods and setting of Private Attributes'''
		if id < 0 or type(id) is not int:
			raise Exception("id is not an integer")
		self.__id = id

		if type(first_name) is not str or len(first_name) is 0:
			raise Exception("first_name is not string")
		self.__first_name = first_name

		for n in date_of_birth[:]:
			if type(n) is not int:
				raise Exception("date_of_birth is not a valid date")

		if date_of_birth[0] not in range(1,13):
			raise Exception("date_of_birth is not a valid date")

		if date_of_birth[1] not in range(1,32):
			raise Exception("date_of_birth is not a valid date")

		self.__date_of_birth = date_of_birth

		if eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")
		self.__eyes_color = eyes_color

		if genre not in Person.GENRES:
			raise Exception("genre is not valid")
		self.__genre = genre

	'''Getters'''
	def get_id(self):
			return self.__id

	def get_eyes_color(self):
		return self.__eyes_color

	def get_genre(self):
		return self.__genre

	def get_first_name(self):
		return self.__first_name


	def __str__(self):
		return __str__(self)




	'''Public Methods'''

	def __str__(self):
		return self.__first_name + " " + self.last_name

	def is_male(self):
		if self.__genre is "Male":
			return "True"

	def age(self):
		today = [5, 20, 2016]
		if today[0] > self.__date_of_birth[0]:
			return today[2] - self.__date_of_birth [2]
		if today[0] == self.__date_of_birth[0] and today[1] < self.__date_of_birth[1]:
				return today[2] - self.__date_of_birth[2]
		else:
			return today[2] - self.__date_of_birth[2] - 1
