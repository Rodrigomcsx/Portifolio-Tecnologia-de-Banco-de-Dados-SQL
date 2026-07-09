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