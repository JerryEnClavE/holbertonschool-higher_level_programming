-- Active: 1729751780644@@localhost@3306
-- Creates the user user_0d_1 with all privileges.
-- Create user if it doesn't already exist
-- Write a script that creates the MySQL server user user_0d_1
-- should have all privileges
-- password should be set to user_0d_1_pwd
-- if user_0d_1 already exists, script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

