CREATE USER IF NOT EXISTS 'microservice'@'localhost' IDENTIFIED BY '123456';

CREATE DATABASE IF NOT EXISTS microservices_auth;
GRANT ALL PRIVILEGES ON microservices_auth.* TO 'microservice'@'localhost';

USE microservices_auth;

CREATE TABLE IF NOT EXISTS users(
    id int NOT null PRIMARY KEY AUTO_INCREMENT, 
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    );

INSERT INTO users(email, password) VALUES ("kevinkone19@gmail.com","kevinKONE");