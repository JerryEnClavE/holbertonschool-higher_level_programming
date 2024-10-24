-- Ensures that the table creation does not fail if the table already exists.
--Defines the id column as an integer, sets a default value of 1, and ensures it cannot be NULL.
--Defines the name column as a variable-length string
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
