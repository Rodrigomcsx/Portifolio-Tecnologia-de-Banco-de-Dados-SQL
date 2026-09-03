DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja;

USE loja;

CREATE TABLE cliente (

	id_cliente INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	cpf CHAR(11) NOT NULL UNIQUE,
	endereco VARCHAR(255),
	telefone VARCHAR(11),
	email VARCHAR(100) UNIQUE,
	data_nasc DATE
    
);

CREATE TABLE produto (

	id_produto INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	categoria VARCHAR(100) NOT NULL,
	preco DECIMAL(10,2) NOT NULL,
	estoque INT NOT NULL

);

CREATE TABLE pedido (

	id_pedido INT PRIMARY KEY AUTO_INCREMENT,
	data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
	id_cliente INT NOT NULL,
	FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)

);

CREATE TABLE item_pedido (

	id_item INT PRIMARY KEY AUTO_INCREMENT,
	quantidade INT NOT NULL,
	valor_unitario DECIMAL(10, 2) NOT NULL,
	id_pedido INT NOT NULL,
	id_produto INT NOT NULL,
	FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
	FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);	