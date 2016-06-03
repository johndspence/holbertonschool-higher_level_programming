PRAGMA foreign_keys = ON;

SELECT DISTINCT last_name FROM Person, TVShowPerson, TVShow WHERE
   Person.id = TVShowPerson.person_id AND TVShowPerson.tvshow_id = TVShow.id
   AND TVShow.name = "Game of Thrones";

SELECT COUNT(id) FROM Person WHERE age > 30;

SELECT Person.id, first_name, last_name, age, color, TVShow.name FROM Person,
	EyesColor, TVShowPerson, TVShow WHERE Person.id = EyesColor.person_id
	AND Person.id = TVShowPerson.person_id AND
	TVShowPerson.tvshow_id = TVShow.id;

SELECT SUM(age) FROM Person;
