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
    endereco            VARCHAR(80),
	status          	BOOLEAN DEFAULT TRUE
);

CREATE TABLE produto (
    produto_id          SERIAL PRIMARY KEY,
    nome                VARCHAR(80),
    descricao           VARCHAR(200),
    quantidade          INTEGER,
    preco               DECIMAL(13, 2),
	status          	BOOLEAN DEFAULT TRUE
);

CREATE TABLE pedido (
    pedido_id       SERIAL PRIMARY KEY,
    usuario_id      INTEGER REFERENCES pessoa(pessoa_id),
    cliente_id      INTEGER REFERENCES pessoa(pessoa_id),
    data_pedido     TIMESTAMP,
	status          BOOLEAN DEFAULT TRUE
);

CREATE TABLE item_pedido (
    produto_id      INTEGER REFERENCES produto(produto_id),
    pedido_id       INTEGER REFERENCES pedido(pedido_id),
    quantidade      INTEGER,
    preco_unitario  DECIMAL(13,2),
    status          BOOLEAN DEFAULT TRUE,
    PRIMARY KEY(produto_id, pedido_id)
);

-- INSERTS

INSERT INTO pessoa (nome, email, senha, telefone, endereco) VALUES ('admin', 'admin', 'pet', '000', '999')

-- SELECTS

SELECT * FROM pessoa;

SELECT * FROM produto;

-- SELECT pd.pedido_id, cli.nome as Cliente, usr.nome as Usuario, pd.data_pedido, COALESCE(SUM(it.preco_unitario * it.quantidade), SUM(it.preco_unitario * it.quantidade), 0)  
-- FROM item_pedido it 
-- RIGHT JOIN pedido pd ON it.pedido_id = pd.pedido_id  
-- INNER JOIN pessoa usr ON usr.pessoa_id = pd.usuario_id 
-- INNER JOIN pessoa cli ON cli.pessoa_id = pd.cliente_id
-- WHERE pd.status = TRUE 
-- GROUP BY (pd.pedido_id, cli.pessoa_id, usr.nome) 
-- ORDER BY (pd.pedido_id) DESC 

-- SELECT p.pedido_id, usr.nome, cli.nome, p.data_pedido
-- FROM pedido p
-- INNER JOIN pessoa usr ON usr.pessoa_id = p.usuario_id
-- INNER JOIN pessoa cli ON cli.pessoa_id = p.cliente_id;