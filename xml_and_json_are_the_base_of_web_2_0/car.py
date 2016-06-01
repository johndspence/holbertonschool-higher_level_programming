
class Car():
	def __init__(self, *args, **kwargs)
		if len(args) > 0 and isinstance(args[0], dict):
			hash = args[0]

			name = hash.get

		if name == None or Name is not string

'''
Private attributes:

name (string)
brand (string)
nb_doors (integer)
Public method:

Constructor: __init__(self, *args, **kwargs)
name is empty or not a string = Exception("name is not a string")
brand is empty or not a string = Exception("brand is not a string")
nb_doors is an integer or <= 0 = Exception("nb_doors is not > 0")
Getter get_name(self)
Getter get_brand(self)
Getter get_nb_doors(self)
to_hash() to return a dictionary data structure who describes the car
__str__(self) to return a string with all information: ":name :brand (:nb_doors)"
guillaume@production-503e7013:$ cat 2-main.py
from car import Car

c = Car(name="Rogue", brand="Nissan", nb_doors=5)
print c
print c.get_brand()
print c.to_hash()

guillaume@production-503e7013:$ python 2-main.py
Rogue Nissan (5)
Rogue
{'nb_doors': 5, 'brand': 'Nissan', 'name': 'Rogue'}
'''
