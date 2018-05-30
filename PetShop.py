import sys
import connect
import importExport
from tkinter import *
import json
import os

class FramePrincipal(Frame):
    _title = "Pet Shop"

    _fontTitle = "SegoeUI 16 bold"
    _fontSubtitle = "SegoeUI 14"
    _fontText = "SegoeUI 12"
    _fontButton = "SegoeUI 10"
    
    _backgroundColor = "#FFFFFF"
    _barColor = "#009688"
    _menuColor = "#f7f7f7"
    _primaryTextColor = "#FFFFFF"
    _secondaryTextColor = "#CCFFFFFF"

    def __init__(self, master=None):
        super().__init__()
        self.master.title(self._title)
        self.master.resizable(False, False)
        #self.master.iconbitmap("res/icon.ico")
        self.master["bg"] = self._backgroundColor
        self.centralizar(1000, 600) # Resolução da tela principal
        self.pack()
        self.addTitle("Menu")
        self.addMenu()
        self.addFrame()

    def addTitle(self, title):
        self.frameTitle = Frame(bg=self._barColor, height=120)
        self.frameTitle.pack(side=TOP, fill=X)

        self.lblTitle = Label(self.frameTitle, bg=self._barColor)
        self.lblTitle["font"] = self._fontTitle
        self.lblTitle["fg"] = self._primaryTextColor
        self.lblTitle["text"] = title
        self.lblTitle.pack(side=LEFT, ipady=20, ipadx=40)

    def addMenu(self):
        self.frameMenu = Frame(bg=self._menuColor)
        self.frameMenu.pack(side=LEFT, fill=Y)

        # self.lblProdutos = Label(self.frameMenu, bg=self._menuColor)
        # self.lblProdutos["text"] = "Usuários"
        # self.lblProdutos.pack(side=TOP, ipady=20, ipadx=60)

        self.btnUsuarios = Button(self.frameMenu, bg=self._menuColor)
        self.btnUsuarios["text"] = "Clientes"
        self.btnUsuarios["font"] = self._fontButton
        self.btnUsuarios["command"] = self.btnUsuariosClick
        self.btnUsuarios.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnProdutos = Button(self.frameMenu, bg=self._menuColor)
        self.btnProdutos["text"] = "Produtos"
        self.btnProdutos["font"] = self._fontButton
        self.btnProdutos["command"] = self.btnProdutosClick
        self.btnProdutos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnPedidos = Button(self.frameMenu, bg=self._menuColor)
        self.btnPedidos["text"] = "Pedidos"
        self.btnPedidos["font"] = self._fontButton
        self.btnPedidos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnImportar = Button(self.frameMenu, bg=self._menuColor)
        self.btnImportar["text"] = "Importar dados"
        self.btnImportar["font"] = self._fontButton
        self.btnImportar["command"] = self.btnImportaClick
        self.btnImportar.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnExportar = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnExportar["text"] = "Exportar dados"
        self.btnExportar["font"] = self._fontButton
        self.btnExportar["command"] = self.btnExportarClick
        self.btnExportar.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnSobre = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnSobre["text"] = "Sobre" 
        self.btnSobre["font"] = self._fontButton
        self.btnSobre["command"] = self.btnSobreClick
        self.btnSobre.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        self.btnSair = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnSair["text"] = "Sair"
        #self.btnSair.configure(state = "normal", relief="raised", bg = "red")
        self.btnSair.bind("<Enter>", self.on_enter)
        self.btnSair.bind("<Leave>", self.on_leave)
        #self.btnSair.config(highlightthickness=10)
        #self.btnSair.config(highlightbackground=self._menuColor)
        self.btnSair["font"] = self._fontButton
        self.btnSair["command"] = self.btnSairClick
        self.btnSair.pack(side=TOP, ipady=20, ipadx=60, fill=X)

    def on_enter(self, e):
        self.btnSair['background'] = 'red'

    def on_leave(self, e):
        self.btnSair['background'] = 'SystemButtonFace'
        
    def addFrame(self):
        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.lblTst = Label(self.frameMain, bg=self._backgroundColor)
        self.lblTst["text"] = "Teste"
        self.lblTst.pack()

        self.btnTrocar = Button(self.frameMain)
        self.btnTrocar["text"] = "Usuários"
        self.btnTrocar["command"] = self.btnUsuariosClick
        self.btnTrocar.pack()

    def btnUsuariosClick(self):
        self.clientesFrame()
        # self.frameMain.destroy()

        # self.frameMain = Frame(bg=self._backgroundColor)
        # self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        # self.lblUsuario = Label(self.frameMain, bg=self._backgroundColor)
        # self.lblUsuario["text"] = "Usuários"
        # self.lblUsuario.pack(side=LEFT)

    # Commands

    def btnProdutosClick(self):
        self.produtosFrame()

    def btnImportaClick(self):
        self.importaFrame()

    def btnSobreClick(self):
        self.sobreFrame()

    def btnExportarClick(self):
        self.exportarFrame()

    # Frames

    def sobreFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblSobre = Label(self.frameSub, bg=self._backgroundColor)
        self.lblSobre["text"] = "Sobre"
        self.lblSobre["font"] = self._fontSubtitle
        self.lblSobre.pack(side=TOP, ipady=20, ipadx=40)

        self.frameTema = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameTema.pack(side=TOP, fill=Y, anchor=W, ipadx=60)

        self.lblTema = Label(self.frameTema, bg=self._backgroundColor)
        self.lblTema["text"] = "Tema"
        self.lblTema["font"] = self._fontText
        self.lblTema.pack(side=TOP, fill=Y, anchor=W, ipadx=60, pady=5)

        self.lblTemaInfo = Label(self.frameTema, bg=self._backgroundColor)
        self.lblTemaInfo["justify"] = LEFT
        self.lblTemaInfo["text"] = "O tema escolhido pela dupla é o de Pet Shop."
        self.lblTemaInfo.pack(side=TOP, ipadx=10)

        self.frameApp = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameApp.pack(side=TOP, fill=Y, anchor=W, ipadx=60, pady=35)

        self.lblApp = Label(self.frameApp, bg=self._backgroundColor)
        self.lblApp["text"] = "Objetivo"
        self.lblApp["font"] = self._fontText
        self.lblApp.pack(side=TOP, fill=Y, anchor=W, ipadx=60, pady=5)

        self.lblAppInfo = Label(self.frameApp, bg=self._backgroundColor)
        self.lblAppInfo["justify"] = LEFT
        self.lblAppInfo["text"] = "O prosósito da aplicação é auxiliar o controle e gerenciamento de um estabelecimento que possua o intuito de\n comercializar produtos como ração e acessórios para animais."
        self.lblAppInfo.pack(side=TOP, ipadx=10)

        self.frameDevs = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDevs.pack(side=TOP, fill=Y, expand=True, anchor=W, ipadx=60)

        self.lblDevs = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDevs["text"] = "Desenvolvedores"
        self.lblDevs["font"] = self._fontText
        self.lblDevs.pack(side=TOP, anchor=W, ipadx=60, pady=5)

        self.lblDev1 = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDev1["justify"] = LEFT
        self.lblDev1["text"] = "%-25s RA: %-14s" %("Fernando Marchetti", "2840481523011")
        self.lblDev1.pack(side=TOP, ipadx=10)

        self.lblDev2 = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDev2["justify"] = LEFT
        self.lblDev2["text"] = "%-25s  RA: %-14s" %("Vitor Xavier de Souza", "2840481523039")
        self.lblDev2.pack(side=TOP, ipadx=10)

    def importaFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblimporta = Label(self.frameSub, bg=self._backgroundColor)
        self.lblimporta["text"] = "Importar dados para Json"
        self.lblimporta["font"] = self._fontSubtitle
        self.lblimporta.pack(side=TOP, ipady=20, ipadx=40)

        self.lblimporta = Frame(self.frameMain, bg=self._backgroundColor)
        self.lblimporta.pack(anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        #importados = {}
        importados = []
        trasferencia = connect.importaDados()
        print(trasferencia)
        # for row in trasferencia:
        #     #i = 0
        #     importados.append({"id": row[0], "nome": row[1], "email": row[2], "senha": row[3], "telefone": row[4], "endereco": row[5]})        
        #     #importados["pessoa%d" %i] = {"id": row[0], "nome": row[1], "email": row[2], "senha": row[3], "telefone": row[4], "endereco": row[5]}
        #     # i = i +1
        # f = open("C:/Users/Elisa Yoko/Desktop/output.json","w")
        # json.dump(importados,f,sort_keys=True,indent=4)
        # f.close()

    def clientesFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblClientes = Label(self.frameSub, bg=self._backgroundColor)
        self.lblClientes["text"] = "Clientes"
        self.lblClientes["font"] = self._fontSubtitle
        self.lblClientes.pack(side=TOP, ipady=20, ipadx=40)

        self.frameClientes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameClientes.pack(anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        scrollY = Scrollbar(self.frameClientes, orient=VERTICAL)

        self.listClientes = Listbox(self.frameClientes, yscrollcommand=scrollY.set)
        self.listClientes["height"] = 10
        self.listClientes["selectmode"] = SINGLE

        self.carregaClientes()
        self.listClientes.bind("<<ListboxSelect>>", self.onClienteSelected)

        self.listClientes.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listClientes.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.frameClientesCommands = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameClientesCommands.pack(side=BOTTOM, fill=X, expand=True, padx=50)
        
        self.btnDeleteCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnDeleteCliente["text"] = "Remover"
        self.btnDeleteCliente["command"] = self.btnInativaPessoaClick
        self.btnDeleteCliente["font"] = self._fontButton
        self.btnDeleteCliente.pack(side=RIGHT, ipady=5, ipadx=10)

        self.btnUpdateCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnUpdateCliente["text"] = "Atualizar"
        self.btnUpdateCliente["font"] = self._fontButton
        self.btnUpdateCliente["command"] = self.btnUpdateClienteClick
        self.btnUpdateCliente.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnAddCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnAddCliente["text"] = "Adicionar"
        self.btnAddCliente["font"] = self._fontButton
        self.btnAddCliente.pack(side=RIGHT, ipady=5, ipadx=10)

    def produtosFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblProdutos = Label(self.frameSub, bg=self._backgroundColor)
        self.lblProdutos["text"] = "Produtos"
        self.lblProdutos["font"] = self._fontSubtitle
        self.lblProdutos.pack(side=TOP, ipady=20, ipadx=40)

        self.frameProdutos = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdutos.pack(anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        scrollY = Scrollbar(self.frameProdutos, orient=VERTICAL)

        self.listProdutos = Listbox(self.frameProdutos, yscrollcommand=scrollY.set)
        self.listProdutos["height"] = 10
        self.listProdutos["selectmode"] = SINGLE

        self.carregaProdutos()
        #self.listProdutos.bind("<<ListboxSelect>>", self.onProdutoSelected)

        self.listProdutos.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listProdutos.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.frameProdutosCommands = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdutosCommands.pack(side=BOTTOM, fill=X, expand=True, padx=50)
        
        self.btnDeleteProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnDeleteProduto["text"] = "Remover"
        self.btnDeleteProduto["command"] = self.btnInativaProdutoClick
        self.btnDeleteProduto["font"] = self._fontButton
        self.btnDeleteProduto.pack(side=RIGHT, ipady=5, ipadx=10)

        self.btnUpdateProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnUpdateProduto["text"] = "Atualizar"
        self.btnUpdateProduto["font"] = self._fontButton
        #self.btnUpdateProduto["command"] = self.btnUpdateProdutoClick
        self.btnUpdateProduto.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnAddProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnAddProduto["text"] = "Adicionar"
        self.btnAddProduto["font"] = self._fontButton
        self.btnAddProduto.pack(side=RIGHT, ipady=5, ipadx=10)

    def exportarFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblExportar = Label(self.frameSub, bg=self._backgroundColor)
        self.lblExportar["text"] = "Exportar dados"
        self.lblExportar["font"] = self._fontSubtitle
        self.lblExportar.pack(side=TOP, ipady=20, ipadx=40)

        self.frameExpName = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpName.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblExpName = Label(self.frameExpName, bg=self._backgroundColor)
        self.lblExpName["text"] = "Nome do arquivo"
        self.lblExpName["font"] = self._fontText
        self.lblExpName.pack(side=TOP, fill=Y, anchor=W)

        self.entryExpName = Entry(self.frameExpName, bg=self._backgroundColor)
        self.entryExpName.insert(0, "backup")
        self.entryExpName.pack(side=TOP, fill=X, padx=15, pady=5)

        self.frameExpPath = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpPath.pack(anchor=N, fill=BOTH, padx=60, ipadx=60, pady=35)

        self.lblExpPath = Label(self.frameExpPath, bg=self._backgroundColor)
        self.lblExpPath["text"] = "Caminho para exportar os dados"
        self.lblExpPath["font"] = self._fontText
        self.lblExpPath.pack(side=TOP, fill=Y, anchor=W)

        self.entryExpPath = Entry(self.frameExpPath, bg=self._backgroundColor)
        self.entryExpPath.insert(0, os.path.join(os.sep, os.environ["SYSTEMDRIVE"], os.environ["HOMEPATH"], "Desktop"))
        self.entryExpPath.pack(side=TOP, fill=X, padx=15, pady=5)

        self.frameExportar = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExportar.pack(side=TOP, fill=Y, anchor=W, ipadx=60, padx=60)

        self.lblExpTudo = Label(self.frameExportar, bg=self._backgroundColor)
        self.lblExpTudo["text"] = "Exportar dados"
        self.lblExpTudo["font"] = self._fontText
        self.lblExpTudo["justify"] = LEFT
        self.lblExpTudo.pack(side=TOP, anchor=W, pady=5)

        self.lblExportarTudo = Label(self.frameExportar, bg=self._backgroundColor)
        self.lblExportarTudo["justify"] = LEFT
        self.lblExportarTudo["text"] = "Exporta os dados armazenados no sistema em um arquivo no formato JSON, que pode possui o conteúdo das tabelas \nPessoa, Produto, Pedido ou ItemPedido, além de possibilitar a exportação de todos os dados."
        self.lblExportarTudo.pack(side=TOP, fill=Y, anchor=W, ipadx=10)

        self.frameExpTypes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpTypes.pack(side=TOP, fill=Y, anchor=N, ipadx=60, padx=60, pady=10)

        expTypes = ["Tudo", "Pessoas", "Produtos", "Pedidos", "ItensPedidos"]
        self.expTypeVar = StringVar()
        for item in expTypes:
            rdb = Radiobutton(self.frameExpTypes, bg=self._backgroundColor)
            rdb["text"] = item
            rdb["variable"] = self.expTypeVar
            #rdb["command"] = self.onRadioSelect
            rdb["value"] = item
            rdb.pack(side=LEFT, anchor=N, ipadx=8)
        self.expTypeVar.set("Tudo")

        self.btnExportarDados = Button(self.frameMain, bg=self._backgroundColor)
        self.btnExportarDados["text"] = "Exportar"
        self.btnExportarDados["command"] = self.btnExportarDadosClick
        self.btnExportarDados.pack(side=TOP, fill=Y, anchor=N, padx=60)

    def btnInativaProdutoClick(self):
        cod = self.getSelectedProduto()
        connect.inativaProduto(cod)
        self.carregaProdutos()

    def btnInativaPessoaClick(self):
        cod = self.getSelectedPessoa()
        connect.inativaPessoa(cod)
        self.carregaClientes()

    def onClienteSelected(self, event):
        cod = self.getSelectedPessoa()
        print("Id: %s" %str(cod))

    def btnExportarDadosClick(self):
        if (self.expTypeVar.get() == "Tudo"):
            importExport.exportarBanco(self.entryExpName.get(), self.entryExpPath.get())
        elif (self.expTypeVar.get() == "Pessoas"):
            importExport.exportarPessoas(self.entryExpName.get(), self.entryExpPath.get())
        elif (self.expTypeVar.get() == "Produtos"):
            importExport.exportarProdutos(self.entryExpName.get(), self.entryExpPath.get())
        elif (self.expTypeVar.get() == "Pedidos"):
            importExport.exportarPedidos(self.entryExpName.get(), self.entryExpPath.get())
        elif (self.expTypeVar.get() == "ItensPedidos"):
            importExport.exportarItens(self.entryExpName.get(), self.entryExpPath.get())

    def btnUpdateClienteClick(self):
        cod = self.getSelectedPessoa()
        print("Id: " + str(cod))

    def getSelectedPessoa(self):
        pos = self.listClientes.curselection()
        item = self.listClientes.get(pos)
        return int(item[3:7])

    def getSelectedProduto(self):
        pos = self.listClientes.curselection()
        item = self.listClientes.get(pos)
        return int(item[3:7])

    def btnSairClick(self):
        sys.exit(0)

    # Atualiza listas

    def carregaClientes(self):
        clientes = connect.selectPessoas()
        self.listClientes.delete(0, END)
        for item in clientes:
            self.listClientes.insert(END, "Id: %-4d Nome: %-30s Email: %-25s Telefone: %-16s Endereco: %-40s" %(item[0], item[1], item[2], item[3], item[4]))


    def carregaProdutos(self):
        produtos = connect.selectProdutos()
        self.listProdutos.delete(0, END)
        for item in produtos:
            self.listProdutos.insert(END, "Id: %-4d Nome: %-30s Descrição: %-40s Quantidade: %-8s Preço: %-10s" %(item[0], item[1], item[2], item[3], item[4]))

    # Auxiliar

    def centralizar(self, largura, altura):
        px = int((self.master.winfo_screenwidth() - largura) / 2)
        py = int((self.master.winfo_screenheight() - altura) / 2)
        self.master.geometry("{}x{}+{}+{}".format(largura, altura, px, py))

app = FramePrincipal()
app.mainloop()