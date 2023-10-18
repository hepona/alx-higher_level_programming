-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT states.id, cities.name FROM states, cities
WHERE cities.id = states.id 
ORDER BY cities.id;
