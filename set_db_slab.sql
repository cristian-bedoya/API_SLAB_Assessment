CREATE DATABASE IF NOT EXISTS db_slab;
CREATE user IF NOT EXISTS 'user_slab'@'localhost' identified BY 'pswd_slab';
GRANT usage ON *.* TO 'user_slab'@'localhost';
GRANT all privileges ON db_slab.* TO 'user_slab'@'localhost';