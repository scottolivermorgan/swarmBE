-- CREATE DATABASE swarm_labs

USE swarm_labs;

-- Drop all tables if they exist

IF OBJECT_ID('[dbo].[Employee]','U') IS NOT NULL
DROP TABLE [dbo].[Employee]
GO

-- Create the table in the specified schema
CREATE TABLE [dbo].[Employee]
(
    [id] INT NOT NULL IDENTITY(1,1) PRIMARY KEY
    [name] VARCHAR(320) NOT NULL,
)