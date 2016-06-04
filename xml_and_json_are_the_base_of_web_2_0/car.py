import json

class Car():
	''' Constructor for car using multiple arguments'''
	def __init__(self, *args, **kwargs):
		if len(args) > 0 and isinstance(args[0], dict):
			hash = args[0]
			name = hash.get('name')
			brand = hash.get('brand')
			nb_doors = hash.get('nb_doors')
		else:
			name = kwargs.get('name')
			brand = kwargs.get('brand')
			nb_doors = kwargs.get('nb_doors')

		'''Error checking'''
		if name == None or not isinstance(name, str):
			raise Exception("name is not a string")
		if brand == None or not isinstance(brand, str):
			raise Exception("brand is not a string")
		if nb_doors < 1 or not isinstance(nb_doors, int):
			raise Exception("nb_doors is not > 0")

		'''Setters'''
		self.__name = name
		self.__brand = brand
		self.__nb_doors = nb_doors

	'''Public Methods'''
	def get_name(self):
		return self.__name
	def get_brand(self):
		return self.__brand
	def get_nb_doors(self):
		return self.__nb_doors
	def to_hash(self):
		return {'name':self.__name, 'brand':self.__brand,
				'nb_doors':self.__nb_doors}
	def __str__(self):
		return self.__name + " " + self.__brand + " " \
				+ "(" + str(self.__nb_doors) + ")"
	def set_nb_doors(self, number):
		self.__nb_doors = number
	def to_json_string(self):
		return str([{"nb_doors":self.__nb_doors, "brand": self.__brand, \
					"name": self.__name}])
	''' Method to create xml_node using the Document() class from
		from xml.dom.minidom import Document'''
	def to_xml_node(self, doc):
		car = doc.createElement('car')
		doc.appendChild(car)
		car.setAttribute('nb_doors', str(self.__nb_doors))
		name = doc.createElement('name')
		car.appendChild(name)
		cdata = doc.createCDATASection(self.__name)
		#namec = doc.createElement('![CDATA[' + str(self.__name) + ']')
		name.appendChild(cdata)
		brand = doc.createElement('brand')
		brand_title = doc.createTextNode(self.__brand)
		brand.appendChild(brand_title)
		car.appendChild(brand)
		return car
