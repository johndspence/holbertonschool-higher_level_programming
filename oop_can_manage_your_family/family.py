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
		'kind': self.__class__.__name__
		}

		if hasattr(self, 'last_name'):
			data['last_name'] = self.last_name
		else:
			data['last_name'] = "unknown"

		return data

	def load_from_json(self, json):
		if type(json) != dict:
			raise Exception("json is not valid")
		for i in json:
			if i == "id":
				self.__id = json[i]
			if i == "first_name":
				self.__eyes_color = json[i]
			if i == "date_of_birth":
				self.__date_of_birth = json[i]
			if i == "first_name":
				self.__first_name = json[i]
			if i == "last_name":
				self.__last_name = json[i]

'''subclasses'''
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
	def can_run(self):
		return False
	def need_help(self):
		return False
	def is_young(self):
		return True
	def can_vote(self):
		return False

class Adult(Person):
	def can_run(self):
		return True
	def need_help(self):
		return False
	def is_young(self):
		return False
	def can_vote(self):
		return True

class Senior(Person):
	def can_run(self):
		return False
	def need_help(self):
		return True
	def is_young(self):
		return False
	def can_vote(self):
		return True

'''Methods outside class'''
def save_to_file(list, filename):
	for i in range(0, len(list)):
		if type(list[i]) != dict:
			kind = type(list[i])
			list[i] = list[i].json()
			list[i]['kind'] = kind.__name__
	target = open(filename, 'w')
	list_dump = json.dumps(list)
	target.write(list_dump)
	target.close()

def load_from_file(filename):
	if type(filename) != str or os.path.isfile(filename) != True:
		raise Exception("filename is not valid or doesn't exist")
	with open(filename) as my_fam:
		data = json.load(my_fam)
	list_persons = []
	for d in data:
		if d['kind'] == "Adult":
			p = Adult(0, 'bill',[12,12,12], "Male", "Blue")
		if d['kind'] == "Baby":
			p = Adult(0, 'bob',[12,12,12], "Male", "Blue")
		if d['kind'] == "Senior":
			p = Senior(0, 'brad',[12,12,12], "Male", "Blue")
		if d['kind'] == "Teenager":
			p = Teenager(0, 'buck',[12,12,12], "Male", "Blue")
		else:
			p = Person(0, 'bud',[12,12,12], "Male", "Blue")
		p.load_from_json(d)
	return list_persons
