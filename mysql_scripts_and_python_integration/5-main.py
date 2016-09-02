#!/usr/bin/python

#mysql python connection object
import mysql.connector

#connect to database
connection = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5', host='173.246.108.142',port='3306',
database='Project_169')

#use cursor method
cursor = connection.cursor()

#1st query for show
get_show_query = ("SELECT TVShow.name FROM TVShow ORDER BY TVShow.name ASC")
cursor.execute(get_show_query)

#Put shows into an object
TVShow_names = cursor.fetchall()

#Loop throught TVShow_names object, printing each one
for TVShowname in TVShow_names:
	print TVShowname[0] + ":"

	#2nd query for seasons, also put into an object
	get_season_query = ("SELECT Season.number FROM Season \
	JOIN TVShow on Season.tvshow_id = TVShow.id \
	WHERE TVShow.name = '" + TVShowname[0] + "' ORDER BY Season.number ASC;")
	cursor.execute(get_season_query)
	Seasons = cursor.fetchall()

	#Loop throught Seasons object and print each Season
	for Season in Seasons:
		print "\tSeason " + str(Season[0]) + ":"

		#Third query for episodes, also put into object
		get_episode_query = ("SELECT Episode.number, Episode.name \
		FROM Episode JOIN Season on Season.id = Episode.season_id \
		JOIN TVShow on Season.tvshow_id = TVShow.id \
		WHERE Season.number = '" + str(Season[0]) + "'\
		AND TVShow.name = '" + TVShowname[0] + "'\
		ORDER BY Episode.number;")

		cursor.execute(get_episode_query)
		Episodes = cursor.fetchall()

		#Tab twice and print each episode 0 1 ;2, 3 etc
		for episode in Episodes:
			print "\t\t" + str(episode[0]) + ": " + (episode[1])

connection.close()
