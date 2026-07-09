CREATE DATABASE loja;

USE loja;

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100)
);

CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
);

CREATE TABLE itens_pedido (
    id INT PRIMARY KEY AUTO_INCREMENT
    id_pedido INT,
    id_produto INT,
    quantidade INT,

    FOREIGN KEY (id_pedido)
        REFERENCES pedidos(id),

    FOREIGN KEY (id_produto)
        REFERENCES produtos(id)
);

INSERT INTO clientes (nome) VALUES
('João'),
('Maria');

INSERT INTO produtos (nome, preco) VALUES
('Mouse',50),
('Teclado',100),
('Monitor',800);

INSERT INTO pedidos (id_cliente) VALUES
(1),
(2);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade) VALUES
(1,1,1),
(1,2,1),
(2,3,1);