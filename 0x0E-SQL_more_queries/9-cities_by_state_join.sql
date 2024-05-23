-- 9 cities
SELECT  cities.id, cities.name, states.name FROM cities LEFT JOIN states 
ON states.id = cities.state_id ORDER BY cities.id;

