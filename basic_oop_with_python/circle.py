from math import exp

''' Class '''
class Circle():

	''' Constructor '''
	def __init__(self, radius):
		self.__radius = radius

	''' Setter '''
	def set_radius(self, radius):
		self.__radius = radius

	def set_name(self, name):
		self.name = name

	def set_center(self, center):
		self.__center = center

	def set_color(self, color):
		self.__color = color

	def area(self):
		return (3.14 * (pow(self.__radius, 2)))

	''' Getter '''
	def get_radius(self, radius):
		self.__radius = radius

	def get_name(self, name):
		self.name = name

	def get_center(self, color):
		self.__center = name

	def get_color(self, color):
		self.__color = color

	def area(self):
		return (3.14159265359 * (pow(self.__radius, 2)))
