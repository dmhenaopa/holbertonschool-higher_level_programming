-- Creates the table unique_id on your MySQL server.
-- unique_id description: id INT with the default value 1 and must be unique.
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
