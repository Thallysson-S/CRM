create database crm_db;
use crm_db;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    endereco VARCHAR(255),
    telefone VARCHAR(20)
);
