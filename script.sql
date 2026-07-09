DROP DATABASE IF EXISTS loja;

CREATE DATABASE loja;

USE loja;

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(11) NOT NULL,
    endereco VARCHAR(255)
);

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    data_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE itens_pedido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
);

INSERT INTO clientes (nome, email, telefone, endereco) VALUES
('João', 'joao@email.com', '11999999999', 'Rua A, 100'),
('Ana', 'ana@email.com', '11988888888', 'Rua B, 200'),
('Maria', 'maria@email.com', '11977777777', 'Rua C, 300');

INSERT INTO produtos (nome, descricao, preco, estoque) VALUES
('Mouse', 'Mouse ótico USB', 49.99, 30),
('Teclado', 'Teclado mecânico RGB', 99.99, 10),
('Monitor', 'Monitor 24" Full HD', 899.99, 5);

INSERT INTO pedidos (id_cliente, data_pedido, total) VALUES
(1, CURRENT_TIMESTAMP, 0),
(2, CURRENT_TIMESTAMP, 0),
(3, CURRENT_TIMESTAMP, 0);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1,1,1,49.99),
(2,2,1,99.99),
(3,3,2,899.99);