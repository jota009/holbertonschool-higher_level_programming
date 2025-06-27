-- Task 4: Create if_not_null with id defaulting to 1 and a name column
CREATE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1, name VARCHAR(256));
