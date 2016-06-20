\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT TVShow.name
FROM TVShow JOIN Season on TVShow.id = Season.tvshow_id
GROUP BY TVShow.name
HAVING count(Season.id) > 3;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name
FROM TVShow JOIN TVShowGenre on TVShow.id = TVShowGenre.tvshow_id
JOIN Genre on TVShowGenre.genre_id = Genre.id
WHERE Genre.name = 'Comedy'
GROUP BY TVShow.name
ORDER BY TVShow.name;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name
FROM Actor JOIN TVShowActor on Actor.id = TVShowActor.actor_id
JOIN TVShow on TVShowActor.tvshow_id = TVShow.id
WHERE TVShow.name = 'The Big Bang Theory'
ORDER BY Actor.name;

\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name, count(TVShow.id) as 'nb_tvshows'
FROM Actor JOIN TVShowActor on Actor.id = TVShowActor.actor_id
JOIN TVShow on TVShowActor.tvshow_id = TVShow.id
GROUP BY Actor.name
ORDER BY nb_tvshows DESC
LIMIT 10;
