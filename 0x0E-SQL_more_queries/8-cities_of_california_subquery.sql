-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Results must be sorted in ascending order by cities.id

SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT cities.id
FROM cities
WHERE name = California;)
ORDER BY cities.id ASC;
