-- Task 1: Create user_0d_1 with all privileges, if they don't already exist

-- 1. Create the account (no error if it already exists)
CREATE USER IF NOT EXISTS
    'user_0d_1'@'localhost'
IDENTIFIED BY
    'user_0d_1_pwd';

-- 2. Grant full privileges on every database and table
GRANT ALL PRIVILEGES
    ON *.*
    TO 'user_0d_1'@'localhost'
    WITH GRANT OPTION; -- allows the user to grant privileges to others

-- 3. Reload the privilege tables so changes take effect immediately
FLUSH PRIVILEGES;
