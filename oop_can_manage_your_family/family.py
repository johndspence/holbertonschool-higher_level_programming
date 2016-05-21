import json
import os.path

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


	'''Public Methods'''
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

	def __str__(self):
		return self.__first_name + " " + self.last_name
	def __lt__(self, other):
		return self.age() < other.age()
	def __le__(self, other):
		return self.age() <= other.age()
	def __eq__(self, other):
		return self.age() == other.age()
	def __ne__(self, other):
		return self.age() >= other.age()
	def __gt__(self, other):
		return self.age() > other.age()

	def json(self):
		data = {
		'id': self.__id,
		'eyes_color': self.__eyes_color,
		'genre': self.__genre,
		'date_of_birth': self.__date_of_birth,
		'first_name': self.__first_name,
		'last_name': self.lastname,
		}

	def load_from_json(self, json):
		if type(json) != dict:
			raise Exception("json is not valid")
			self.__id = json ['id']
			self.__eyes_color = json['eyes_color']
			self.__date_of_birth = json['date_of_birth']
			self.__first_name = json['first_name']
			self.__last_name = json['last_name']

class Baby(Person):
	''' functions can_run, need_help, is_young, can_vote return True or False
		repeated for each subclass Baby, Teenager, Adult, Senior'''
	def can_run(self):
		return False
	def need_help(self):
		return True
	def is_young(self):
		return True
	def can_vote(self):
		return False

class Teenager(Person):
	''' functions can_run, need_help, is_young, can_vote return True or False
		repeated for each subclass Baby, Teenager, Adult, Senior'''
	def can_run(self):
		return False
	def need_help(self):
		return False
	def is_young(self):
		return True
	def can_vote(self):
		return False

class Adult(Person):
	''' functions can_run, need_help, is_young, can_vote return True or False
		repeated for each subclass Baby, Teenager, Adult, Senior'''
	def can_run(self):
		return True
	def need_help(self):
		return False
	def is_young(self):
		return False
	def can_vote(self):
		return True

class Senior(Person):
	''' functions can_run, need_help, is_young, can_vote return True or False
		repeated for each subclass Baby, Teenager, Adult, Senior'''
	def can_run(self):
		return False
	def need_help(self):
		return True
	def is_young(self):
		return False
	def can_vote(self):
		return True


def save_to_file(list, filename):
	return "save to file"

def load_from_file(filename):
		if type(filename) != str or os.path.isfile(filename) != True:
			raise Exception("filename is not valid or doesn't exist")
		with open(filename) as my_fam:
			data = json.load(my_fam)
		my_fam.close()

		data =
		array = []
