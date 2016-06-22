# Queries below as specified in project 169
\! echo "\nList of all tables?"
show tables;

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
SHOW CREATE TABLE TVShow;
SHOW CREATE TABLE Genre;
SHOW CREATE TABLE TVShowGenre;

\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT TVShow.id, TVShow.name from TVShow
ORDER BY TVShow.name;

\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT Genre.id, Genre.name from Genre
ORDER BY name DESC;

\! echo "\nList of Network, only id and name?"
SELECT Network.id, Network.name from Network;

\! echo "\nNumber of episodes in the database?"
SELECT count(id) from Episode;
