import psycopg2 as pg
import models

def initialize():
    global conn
    global cursor
    conn = pg.connect(
            database="petshop",
            user="postgres",
            password="fatec",
            host="127.0.0.1",
            port="5432"
        )
    cursor = conn.cursor()

def finalize():
    global conn
    global cursor
    conn.commit()
    conn.close()

def insertPessoa(user):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO pessoa (nome, email, senha, telefone, endereco) VALUES (%s, %s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (user.nome, user.email, user.senha, user.telefone, user.endereco))
    cursor.execute(sql_values)
    finalize()

def selectPessoas(status=True):
    global conn
    global cursor
    initialize()
    sql = "SELECT * FROM pessoa"
    sql += " WHERE status = TRUE" if status else ""
    cursor.execute(sql)
    result = cursor.fetchall()
    finalize()
    return result

def inativaPessoa(pessoaId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE pessoa SET status = FALSE WHERE pessoa_id = %s"
    sql_values = cursor.mogrify(sql, str(pessoaId))
    cursor.execute(sql_values)
    finalize()

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

def inativaProduto(produtoId):
    global conn
    global cursor
    initialize()
    sql = "UPDATE produto SET status = FALSE WHERE produto_id = %s"
    sql_values = cursor.mogrify(sql, str(produtoId))
    cursor.execute(sql_values)
    finalize()

def insertPedido(pedido):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO pedido (pedido_id, usuario_id, cliente_id, data_pedido) VALUES (%s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (pedido.pedido_id, pedido.usuario_id, pedido.cliente_id, pedido.data_pedido))
    cursor.execute(sql_values)
    finalize()

def insertItemPedido(itemPedido):
    global conn
    global cursor
    initialize()
    sql = "INSERT INTO itemPedido (produto_id, pedido_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
    sql_values = cursor.mogrify(sql, (itemPedido.produto_id, itemPedido.pedido_id, itemPedido.quantidade, itemPedido.preco_unitario))
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
    

p = models.Pessoa()
p.nome = "Usuário 1"
p.email = "usuario@mail.com"
p.senha = "123"
p.telefone = "1234567890"
p.endereco = "Rua 1"

#insertPessoa(p)
selectPessoas()