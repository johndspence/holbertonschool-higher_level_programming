/* Basic Update Statements */ 
Update Person Set age=27 where first_name = 'Jon' and last_name = 'Snow';
Update Person Set age=18 where first_name = 'Walter Junior'
and last_name = 'White';

PRAGMA foreign_keys = ON;

/* Delete a record respecting foreign key relationships */
delete from EyesColor
where exists
	( Select *
	FROM Person where Person.id = EyesColor.person_id
	and first_name='Walter' and last_name='White');

delete from Person where first_name='Walter' and last_name='White';

select * FROM Person order by first_name;
select * FROM EyesColor order by person_id;
