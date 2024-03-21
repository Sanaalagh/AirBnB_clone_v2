-- Creates a MySQL server
--   Database hbnb_test_db
--   User hbnb_test with password hbnb_test_pwd in localhost
--   Grants all privileges for hbnb_test on hbnb_test_db
--   Grants SELECT privilege for hbnb_test on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges for the user on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
