-- Task 5: Create unique_id with id defaulting to 1 and enforced uniqueness
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR (256));
