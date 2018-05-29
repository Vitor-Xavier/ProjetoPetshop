CREATE DATABASE petshop;

DROP TABLE IF EXISTS item_pedido;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS produto;
DROP TABLE IF EXISTS pessoa;

CREATE TABLE pessoa (
    pessoa_id          SERIAL PRIMARY KEY,
    nome                VARCHAR(80),
    email               VARCHAR(60),
    senha               VARCHAR(40),
    telefone            VARCHAR(20),
    endereco            VARCHAR(80)
);

CREATE TABLE produto (
    produto_id          SERIAL PRIMARY KEY,
    nome                VARCHAR(80),
    descricao           VARCHAR(200),
    quantidade          INTEGER,
    preco               DECIMAL(13, 2)
);

CREATE TABLE pedido (
    pedido_id       SERIAL PRIMARY KEY,
    usuario_id      INTEGER REFERENCES pessoa (pessoa_id),
    cliente_id      INTEGER REFERENCES pessoa (pessoa_id),
    data_pedido     TIMESTAMP
);

CREATE TABLE item_pedido (
    produto_id      INTEGER REFERENCES produto(produto_id),
    pedido_id       INTEGER REFERENCES pedido(pedido_id),
    quantidade      INTEGER,
    preco_unitario  DECIMAL(13,2),
    PRIMARY KEY(produto_id, pedido_id)
);

-- DADOS

SELECT * FROM pessoa;

INSERT INTO pessoa (nome, email, senha, telefone, endereco) VALUES ('usr1', 'usr1@mail.com', '12345', '+551690909090', 'Rua Abilio Sampaio, 9666');

SELECT * FROM produto;

INSERT INTO produto (nome, descricao, quantidade, preco) 
VALUES 
('Tigela', 'Tigela para pets', 15, 19.9);