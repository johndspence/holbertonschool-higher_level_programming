#!/usr/bin/python

import mysql.connector

connection = mysql.connector.connect(user='student',
                            password='aLQQLXGQp2rJ4Wy5',
                            host='173.246.108.142',
                            port='3306',
                            database='Project_169')

cursor = connection.cursor()

query = ("SELECT TVShow.name, Season.number, Episode.number, Episode.name FROM TVShow JOIN Season on TVShow.id = Season.tvshow_id JOIN Episode on Season.id = Episode.season_id")

cursor.execute(query)

for (name, season, episode_number, episode_name) in cursor:
    print str(name) + ":"
    print season

connection.close()
print "I think everything worked"
