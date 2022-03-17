-- search califormia
SELECT * FROM states;
SELECT * FROM cities;
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY name ASC;
