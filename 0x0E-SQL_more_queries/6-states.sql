-- create table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT unique AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
	);

