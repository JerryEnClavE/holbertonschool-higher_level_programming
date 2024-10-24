-- Script to create the database hbtn_0d_usa and the table cities
-- The database hbtn_0d_usa will not be created again if it already exists
-- The table cities will not be created again if it already exists
-- The cities table includes:
--    id: INT, unique, auto generated, can’t be null and is a primary key
--    state_id: INT, can’t be null and is a FOREIGN KEY referencing id of the states table
--    name: VARCHAR(256), can’t be null

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the 'cities' table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
