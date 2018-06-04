class Pessoa(object):
    pessoa_id = 0
    nome = ""
    email = ""
    senha = ""
    telefone = ""
    endereco = ""

class Produto(object):
    produto_id = 0
    nome = ""
    descricao = ""
    quantidade = ""
    preco = 0.0

class Pedido(object):
    pedido_id = 0
    usuario_id = 0
    cliente_id = 0
    data_pedido = ""

class ItemPedido(object):
    produto_id = 0
    pedido_id = 0
    quantidade = 0
    preco_unitario = 0.0