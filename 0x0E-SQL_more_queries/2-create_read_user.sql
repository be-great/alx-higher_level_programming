-- create database and user and grant priviliges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE user if not exists 'user_0d_2'@'localhost' identified by 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

