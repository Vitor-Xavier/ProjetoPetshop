import psycopg2 as pg
import psycopg2.extras as pg_ex
import models

def initialize():
    global conn
    global cursor
    conn = pg.connect(
            database="petshop",
            user="postgres",
            password="fatec",
            host="127.0.0.1",
            port="5432",
            cursor_factory=pg_ex.NamedTupleCursor
        )
    cursor = conn.cursor(cursor_factory=pg_ex.NamedTupleCursor)

def finalize():
    global conn
    global cursor
    conn.commit()
    conn.close()

# Pessoa

def insertPessoa(pessoa):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO pessoa (nome, email, senha, telefone, endereco) VALUES (%s, %s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (pessoa.nome, pessoa.email, pessoa.senha, pessoa.telefone, pessoa.endereco))
    cursor.execute(sql_values)
    finalize()

def updatePessoa(pessoa):
    global conn
    global cursor
    initialize()
    sql = "UPDATE pessoa SET nome = %s, email = %s, senha = %s, telefone = %s, endereco = %s WHERE pessoa_id = %s"
    sql_values = cursor.mogrify(sql, (pessoa.nome, pessoa.email, pessoa.senha, pessoa.telefone, pessoa.endereco, pessoa.pessoa_id))
    cursor.execute(sql_values)
    finalize()

def selectPessoas(status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT pessoa_id, nome, email, telefone, endereco FROM pessoa"
    sql += " WHERE status = TRUE" if status else ""
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def selectPessoa(pessoaId, status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT pessoa_id, nome, email, telefone, endereco FROM pessoa WHERE pessoa_id = %s"
    sql += " AND status = TRUE" if status else ""
    sql_values = cursor.mogrify(sql, (str(pessoaId), ))
    cursor.execute(sql_values)
    result = cursor.fetchone()
    finalize()
    return result

def inativaPessoa(pessoaId):
    global conn
    global cursor
    initialize()
    sql = """DO
            $BODY$
            BEGIN
                IF exists(SELECT (1) FROM pessoa where pessoa_id = %s and status = FALSE) THEN
                    UPDATE pessoa SET status = TRUE where pessoa_id = %s;
                ELSE 
                    UPDATE pessoa SET status = FALSE where pessoa_id = %s;
            END IF;
            END
            $BODY$"""
    sql_values = cursor.mogrify(sql, str(pessoaId))
    cursor.execute(sql_values)
    finalize()

# "UPDATE pessoa SET status = FALSE WHERE pessoa_id = %s"

# Produto

def insertProduto(produto):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO produto (nome, descricao, quantidade, preco) VALUES (%s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (produto.nome, produto.descricao, produto.quantidade, produto.preco))
    cursor.execute(sql_values)
    finalize()

def selectProdutos(status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM produto" 
    sql += " WHERE status = TRUE" if status else ""
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def selectProduto(produtoId, status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM produto WHERE produto_id = %s" 
    sql += " AND status = TRUE" if status else ""
    sql_values = cursor.mogrify(sql, (str(produtoId), ))
    cursor.execute(sql_values)
    result = cursor.fetchone()
    finalize()
    return result

def updateProduto(produto):
    global conn
    global cursor
    initialize()
    sql = "UPDATE produto SET nome = %s, descricao = %s, quantidade = %s, preco = %s WHERE produto_id = %s"
    sql_values = cursor.mogrify(sql, (produto.nome, produto.descricao, produto.quantidade, produto.preco, produto.produto_id))
    cursor.execute(sql_values)
    finalize()

def updateProdutoQtd(produtoId, qtd):
    global conn
    global cursor
    initialize()
    select_sql = "SELECT quantidade FROM produto WHERE produto_id = %s"
    select_values = cursor.mogrify(select_sql, (produtoId, ))
    cursor.execute(select_values)
    qtd_atual = cursor.fetchone()[0]
    sql = "UPDATE produto SET quantidade = %s WHERE produto_id = %s"
    sql_values = cursor.mogrify(sql, (int(qtd_atual) + int(qtd), produtoId))
    cursor.execute(sql_values)
    finalize()

def inativaProduto(produtoId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE produto SET status = FALSE WHERE produto_id = %s"
    sql_values = cursor.mogrify(sql, str(produtoId))
    cursor.execute(sql_values)
    finalize()

# Pedido

def insertPedido(pedido):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO pedido (usuario_id, cliente_id, data_pedido, status) VALUES (%s, %s, CURRENT_TIMESTAMP, FALSE)  RETURNING pedido_id"
    sql_values = cursor.mogrify(sql, (pedido.usuario_id, pedido.cliente_id))
    cursor.execute(sql_values)
    pedidoId = cursor.fetchone()[0]
    finalize()
    return pedidoId

def selectPedidos(status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM pedido" 
    sql += " WHERE status = TRUE" if status else ""
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def selectPedido(pedidoId, status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM pedido WHERE pedido_id = %s" 
    sql += " AND status = TRUE" if status else ""
    sql_values = cursor.mogrify(sql, (str(pedidoId), ))
    cursor.execute(sql_values)
    result = cursor.fetchone()
    finalize()
    return result

def updatePedidoCliente(pedidoId, clienteId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE pedido SET cliente_id = %s, status = TRUE WHERE pedido_id = %s" 
    sql_values = cursor.mogrify(sql, (str(clienteId), str(pedidoId)))
    cursor.execute(sql_values)
    finalize()

def selectPedidosJoin(status=True):
    global conn
    global cursor
    initialize()
    sql =  """
        SELECT pd.pedido_id, cli.nome as Cliente, usr.nome as Usuario, pd.data_pedido, COALESCE(SUM(it.preco_unitario * it.quantidade), SUM(it.preco_unitario * it.quantidade), 0)  
        FROM item_pedido it 
        RIGHT JOIN pedido pd ON it.pedido_id = pd.pedido_id  
        INNER JOIN pessoa usr ON usr.pessoa_id = pd.usuario_id 
        INNER JOIN pessoa cli ON cli.pessoa_id = pd.cliente_id
        """
    sql += "WHERE pd.status = TRUE " if status else ""
    sql += """
        GROUP BY (pd.pedido_id, cli.pessoa_id, usr.nome) 
        ORDER BY (pd.pedido_id) DESC
        """
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def inativaPedido(pedidoId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE pedido SET status = FALSE WHERE pedido_id = %s"
    sql_values = cursor.mogrify(sql, (str(pedidoId), ))
    cursor.execute(sql_values)
    finalize()

# Itens

def insertItemPedido(itemPedido):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO item_pedido (produto_id, pedido_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (itemPedido.produto_id, itemPedido.pedido_id, itemPedido.quantidade, itemPedido.preco_unitario))
    cursor.execute(sql_values)
    finalize()

def selectItens(pedidoId, status=True):
    global conn
    global cursor
    initialize()
    sql = """
        SELECT it.produto_id, it.pedido_id, pr.nome, it.quantidade, pr.preco, (it.quantidade * pr.preco)
        FROM item_pedido it
        INNER JOIN produto pr ON it.produto_id = pr.produto_id
        WHERE it.pedido_id = %s AND it.status = TRUE
    """
    sql_values = cursor.mogrify(sql, (str(pedidoId), ))
    cursor.execute(sql_values)
    result = cursor.fetchall()
    finalize()
    return result

def inativaItemPedido(pedidoId, produtoId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE item_pedido SET status = FALSE WHERE pedido_id = %s AND produto_id = %s"
    sql_values = cursor.mogrify(sql, (pedidoId, produtoId))
    cursor.execute(sql_values)
    finalize()

def importaDados():
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM pessoa"
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def login(email, senha):
    global conn
    global cursor
    initialize()
    sql = "SELECT email, senha FROM pessoa WHERE email = %s"
    sql_values = cursor.mogrify(sql, (email, ))
    cursor.execute(sql_values)
    result = cursor.fetchone()
    finalize()
    if (result != None and result[1] == senha):
        return True
    else:
        return False

p = models.Pessoa()
p.nome = "Usuário 1"
p.email = "usuario@mail.com"
p.senha = "123"
p.telefone = "1234567890"
p.endereco = "Rua 1"

#insertPessoa(p)
#selectPessoas()
#login("usuario@mail.com", "123")