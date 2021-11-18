-- Creates the MySQL server user user_0d_1.
-- User has all privileges on your MySQL server.
-- Do nothing If the user user_0d_1 already exists.

CREATE USER IF NOT EXIST 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
