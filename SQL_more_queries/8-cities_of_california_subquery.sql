-- Script to list all the cities of California from the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
