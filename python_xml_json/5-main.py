import json
from car import Car
from xml.dom import minidom

json_string=open('./5-main.json')
json_data=json.loads(json_string.read())

# Create array to hold brands - count later
brands = []

# Create int to hold cumulative number of doors
cumnb_doors = 0

doc = minidom.Document()
cars = doc.createElement('cars')
doc.appendChild(cars)

# Iterate through json_data to pull brands and doors
for i in json_data:
	car = Car(i)

	brand = car.get_brand()
	if brand not in brands:
		brands.append(brand)

	nb_doors = car.get_nb_doors()
	cumnb_doors += nb_doors

	car_xml = car.to_xml_node(doc)
	cars.appendChild(car_xml)


print len(brands)
print cumnb_doors
print Car(json_data[3])
print doc.toxml(encoding='utf-8')
