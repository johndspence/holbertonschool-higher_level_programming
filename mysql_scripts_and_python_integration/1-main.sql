# Queries below as specified in project 169
\! echo "\nNumber of seasons by tvshow_id?"
SELECT Season.tvshow_id, count(id)
FROM Season
GROUP BY Season.tvshow_id;

\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
SELECT Episode.number, count(id)
FROM Episode
GROUP BY Episode.number;

\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
SELECT TVShowGenre.genre_id, count(TVShowGenre.genre_id) AS "occurrences_genre"
FROM TVShowGenre
GROUP BY TVShowGenre.genre_id
ORDER BY count(TVShowGenre.genre_id) DESC
LIMIT 3;

\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
SELECT LOWER(TVShow.name) as name
FROM TVShow
WHERE TVShow.name REGEXP "th";
