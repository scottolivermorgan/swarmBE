-- CREATE DATABASE swarm_labs;
USE swarm_labs;

-- Create the table in the specified schema
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee(  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(320) NOT NULL,
    role VARCHAR(320) NOT NULL,
    img VARCHAR(320) NOT NULL,
    titles VARCHAR(320) NOT NULL,
    bio VARCHAR(320) NOT NULL,
    links VARCHAR(320) NOT NULL,
    PRIMARY KEY(id)
);