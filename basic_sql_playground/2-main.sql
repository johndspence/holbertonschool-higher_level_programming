/* Basic Insert statements in dividual tables without joins */
insert into Person(first_name,last_name,age)VALUES('Jon','Snow','26');
insert into Person(first_name,last_name,age)VALUES('Arya','Stark','12');
select * FROM Person ORDER BY last_name;
