-- Task 2: Create hbtn_0d_2 DB and user_0d_2 with read-only acces

-- 1. Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. Create the user (no error if they already exist)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- 3. Grant only SELECT on the new database
GRANT SELECT ON hbtn_0c_2.* TO 'user_0d_2'@'localhost';

-- 4. Reload privileges so everything takes effect now
FLUSH PRIVILEGES;
