--create a table called id_not_null, but it doesn't enforce
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1, 
  name VARCHAR(256)
);
