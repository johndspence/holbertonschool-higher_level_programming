PRAGMA foreign_keys = ON;

/* Nested Select Statements */
INSERT INTO EyesColor(person_id, color)VALUES((SELECT id FROM Person where
	first_name='Jon'and last_name='Snow'),'Brown');
INSERT INTO EyesColor(person_id, color)VALUES((SELECT id FROM Person where
	first_name='Arya'and last_name='Stark'),'Green');

/* Table Creation */
CREATE TABLE TVShow (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name char (128)
);

CREATE TABLE TVShowPerson (
	tvshow_id INTEGER NOT NULL,
	person_id INTEGER NOT NULL,
	FOREIGN KEY(tvshow_id) REFERENCES TVShow(id)
	FOREIGN KEY(person_id) REFERENCES Person(id)
);

/* Insert rows */
INSERT INTO TVShow(name)VALUES('Homeland');
INSERT INTO TVShow(name)VALUES('The big bang theory');
INSERT INTO TVShow(name)VALUES('Game of Thrones');
INSERT INTO TVShow(name)VALUES('Breaking bad');

/* Insert Rows respecting foreign_keys */
INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='Breaking bad'),(SELECT id FROM Person where
		first_name='Walter Junior' and last_name='White'));

INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='Game of Thrones'),(SELECT id FROM Person where
		first_name='Jaime' and last_name='Lannister'));

INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='The big bang theory'),(SELECT id FROM Person where
		first_name='Sheldon' and last_name='Cooper'));

INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='Game of Thrones'),(SELECT id FROM Person where
		first_name='Tyrion' and last_name='Lannister'));

INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='Game of Thrones'),(SELECT id FROM Person where
		first_name='Jon' and last_name='Snow'));

INSERT INTO TVShowPerson(tvshow_id,person_id)VALUES((SELECT id FROM TVShow
	where name='Game of Thrones'),(SELECT id FROM Person where
		first_name='Arya' and last_name='Stark'));

SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
