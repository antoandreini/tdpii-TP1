-- DROP DATABASE Practica1;
CREATE DATABASE Practica1;

USE Practica1;

DROP TABLE IF EXISTS Clima;
CREATE TABLE Clima (
  `id` INT NOT NULL AUTO_INCREMENT,
  `temperatura` FLOAT NOT NULL,
  `humedad` FLOAT NOT NULL,
  `presion` FLOAT NOT NULL,
  `viento` FLOAT NOT NULL,
  PRIMARY KEY (`id`));

DROP TABLE IF EXISTS Configuracion;
CREATE TABLE Configuracion (
  `clave` VARCHAR(255) NOT NULL,
  `valor` INT NOT NULL,
  PRIMARY KEY (`clave`));


INSERT INTO Configuracion (clave,valor) VALUES ('frecuencia',10);