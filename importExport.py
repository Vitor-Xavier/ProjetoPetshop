import simplejson as json
import connect

def exportarBanco(path):
    itens = connect.selectItens()
    pedidos = connect.selectPedidos()
    produtos = connect.selectProdutos()
    pessoas = connect.selectPessoas()

    db_data = {"Pessoas": pessoas, "Produtos": produtos, "Pedidos": pedidos, "ItensPedido": itens}
    file = open(path, "w")
    json.dump(db_data, file, sort_keys=True, indent=4)

def exportarPessoas(path):
    pessoas = connect.selectPessoas()

    file = open(path, "w")
    json.dump(pessoas, file, sort_keys=True, indent=4)

def exportarProdutos(path):
    produtos = connect.selectProdutos()

    file = open(path, "w")
    json.dump(produtos, file, sort_keys=True, indent=4)

def exportarPedidos(path):
    pedidos = connect.selectPedidos()

    file = open(path, "w")
    json.dump(pedidos, file, sort_keys=True, indent=4)

def exportarItens(path):
    itens = connect.selectItens()

    file = open(path, "w")
    json.dump(itens, file, sort_keys=True, indent=4)