import simplejson as json
import zipfile as zip
import os
import connect
import models
import requests

def exportarBanco(filename, path):
    filename += ".json"
    itens = connect.selectItens()
    pedidos = connect.selectPedidos()
    produtos = connect.selectProdutos()
    pessoas = connect.selectPessoas()

    db_data = {"Pessoas": pessoas, "Produtos": produtos, "Pedidos": pedidos, "ItensPedido": itens}

    try:
        file = open(os.path.join(os.sep, path, filename), "w")
        json.dump(db_data, file, sort_keys=True, indent=4)
        file.close()
        compactarArquivo(filename, path)
        return True
    except Exception:
        return False

def exportarPessoas(filename, path):
    filename += ".json"
    pessoas = connect.selectPessoas()

    try:
        file = open(os.path.join(os.sep, path, filename), "w")
        json.dump(pessoas, file, sort_keys=True, indent=4)
        file.close()
        compactarArquivo(filename, path)
        return True
    except Exception:
        return False

def exportarProdutos(filename, path):
    filename += ".json"
    produtos = connect.selectProdutos()

    try:
        file = open(os.path.join(os.sep, path, filename), "w")
        json.dump(produtos, file, sort_keys=True, indent=4)
        file.close()
        compactarArquivo(filename, path)
        return True
    except Exception:
        return False

def exportarPedidos(filename, path):
    filename += ".json"
    pedidos = connect.selectPedidos()

    try:
        file = open(os.path.join(os.sep, path, filename), "w")
        json.dump(pedidos, file, sort_keys=True, indent=4)
        file.close()
        compactarArquivo(filename, path)
        return True
    except Exception:
        return False

def exportarItens(filename, path):
    filename += ".json"
    itens = connect.selectItens()

    try:
        file = open(os.path.join(os.sep, path, filename), "w")
        json.dump(itens, file, sort_keys=True, indent=4)
        file.close()
        compactarArquivo(filename, path)
        return True
    except Exception:
        return False

def compactarArquivo(filename, path):
    zip_filename, _ = os.path.splitext(filename)
    zip_filename += ".zip"
    zip_path = os.path.join(os.sep, path, zip_filename)
    zf = zip.ZipFile(zip_path, "w")
    os.chdir(path)
    zf.write(filename)
    zf.close()
    os.remove(os.path.join(os.sep, path, filename))

def importarBanco(file_url):
    banco = requests.get(url=file_url)
    carregarPessoas(banco.json()["Pessoas"])
    carregarProdutos(banco.json()["Produtos"])
    carregarPedidos(banco.json()["Pedidos"])
    carregarItensPedidos(banco.json()["ItensPedido"])
    return banco.json()

def importarPessoas(file_url):
    dados = requests.get(url=file_url)
    carregarPessoas(dados)
    return dados

def importarProdutos(file_url):
    dados = requests.get(url=file_url)
    carregarProdutos(dados)
    return dados

def importarPedidos(file_url):
    dados = requests.get(url=file_url)
    carregarPedidos(dados)
    return dados

def importarItensPedidos(file_url):
    dados = requests.get(url=file_url)
    carregarItensPedidos(dados)
    return dados

def carregarPessoas(pessoas):
    for pessoa in pessoas:
        p = models.Pessoa()
        p.pessoa_id = pessoa["pessoa_id"]
        p.nome = pessoa["nome"]
        p.email = pessoa["email"]
        p.senha = pessoa["senha"]
        p.telefone = pessoa["telefone"]
        connect.insertPessoa(p)

def carregarProdutos(produtos):
    for produto in produtos:
        p = models.Produto()
        p.produto_id = produto["produto_id"]
        p.nome = produto["nome"]
        p.quantidade = produto["quantidade"]
        p.preco = produto["preco"]
        p.descricao = produto["descricao"]
        connect.insertProduto(p)

def carregarPedidos(pedidos):
    for pedido in pedidos:
        p = models.Pedido()
        p.pedido_id = pedido["pedido_id"]
        p.cliente_id = pedido["cliente_id"]
        p.usuario_id = pedido["usuario_id"]
        p.data_pedido = pedido["data_pedido"]
        connect.insertPedido(p)

def carregarItensPedidos(itens):
    for item in itens:
        it = models.ItemPedido()
        it.pedido_id = item["pedido_id"]
        it.produto_id = item["produto_id"]
        it.quantidade = item["quantidade"]
        it.preco_unitario = item["preco_unitario"]
        connect.insertItemPedido(it)

# https://raw.githubusercontent.com/Vitor-Xavier/JsonTst/master/banco.json