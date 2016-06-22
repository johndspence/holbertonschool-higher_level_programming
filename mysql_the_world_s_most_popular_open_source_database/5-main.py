#!/usr/bin/python

import mysql.connector

connection = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5', host='173.246.108.142',port='3306',
database='Project_169')

cursor = connection.cursor()

query = ("SELECT TVShow.name FROM TVShow ORDER BY TVShow.name ASC")
cursor.execute(query)

TVShow_names = cursor.fetchall()

for (name, season, episode_number, episode_name) in cursor:
	print str(name) + ":"
	print season

connection.close()
print "I think everything worked"
