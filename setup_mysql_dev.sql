-- Creates a MySQL server
--   Database hbnb_dev_db
--   User hbnb_dev with password hbnb_dev_pwd in localhost
--   Grants all privileges for hbnb_dev on hbnb_dev_db
--   Grants SELECT privilege for hbnb_dev on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges for the user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
