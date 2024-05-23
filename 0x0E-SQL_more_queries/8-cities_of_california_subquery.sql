-- lists all cities
SELECT id, name from cities where state_id = ( select id from states where name = 'California') order by id ASC;
