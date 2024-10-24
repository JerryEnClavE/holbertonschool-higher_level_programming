-- Check that the table does not exist with IF NOT EXISTS
-- Create the id column as INT, with a default value of 1 and NOT NULL.
-- should not fail if exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);