import simplejson as json
import zipfile as zip
import os
import connect

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