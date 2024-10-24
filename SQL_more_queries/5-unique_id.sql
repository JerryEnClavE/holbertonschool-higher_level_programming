-- 5-unique_id.sql
-- Creates the 'unique_id' table to store unique identifiers and associated names.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
