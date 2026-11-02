CREATE DATABASE exampledb;
CREATE USER 'exampleuser'@'localhost' IDENTIFIED BY 'pimylifeup';
USE exampledb;
CREATE TABLE Sensorstats (date_time VARCHAR(50), irsensorstat FLOAT);
GRANT ALL PRIVILEGES ON exampledb.* TO 'exampleuser'@'localhost';
FLUSH PRIVILEGES;
quit
