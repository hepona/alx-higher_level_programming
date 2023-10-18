-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT states.id, cities.name FROM cities, states
WHERE states.name = 'California'
ORDER BY cities.id;
