import sys
import connect
import models
import importExport
from tkinter import *
import json
import os
import tkinter

class FramePrincipal(Frame):
    _title = "Pet Shop"

    _fontTitle = "SegoeUI 16 bold"
    _fontSubtitle = "SegoeUI 14"
    _fontText = "SegoeUI 12"
    _fontButton = "SegoeUI 10"
    _fontBody = "SegoeUI 10"
    
    _backgroundColor = "#FFFFFF"
    _barColor = "#009688"
    _menuColor = "#f7f7f7"
    _buttonHoverColor = "#e0e0e0"
    _primaryTextColor = "#FFFFFF"
    _bodyTextColor = "#323232"
    _secondaryTextColor = "#CCFFFFFF"

    #Inicializando o Menu Principal
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

    def centralizar(self, largura, altura):
        px = int((self.master.winfo_screenwidth() - largura) / 2)
        py = int((self.master.winfo_screenheight() - altura) / 2)
        self.master.geometry("{}x{}+{}+{}".format(largura, altura, px, py))

    #Titulo Menu
    def addTitle(self, title):
        self.frameTitle = Frame(bg=self._barColor, height=120)
        self.frameTitle.pack(side=TOP, fill=X)

        self.lblTitle = Label(self.frameTitle, bg=self._barColor)
        self.lblTitle["font"] = self._fontTitle
        self.lblTitle["fg"] = self._primaryTextColor
        self.lblTitle["text"] = title
        self.lblTitle.pack(side=LEFT, ipady=20, ipadx=40)
   


    #Menus Principais Laterais
    def addMenu(self):
        self.frameMenu = Frame(bg=self._menuColor)
        self.frameMenu.pack(side=LEFT, fill=Y)

        #Botão Usuarios
        self.btnUsuarios = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnUsuarios["text"] = "Clientes"
        self.btnUsuarios["font"] = self._fontButton
        self.btnUsuarios["fg"] = self._bodyTextColor
        self.btnUsuarios["command"] = self.btnUsuariosClick
        self.btnUsuarios.bind("<Enter>", self.on_enter)
        self.btnUsuarios.bind("<Leave>", self.on_leave)
        self.btnUsuarios.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Produtos
        self.btnProdutos = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnProdutos["text"] = "Produtos"
        self.btnProdutos["font"] = self._fontButton
        self.btnProdutos["fg"] = self._bodyTextColor
        self.btnProdutos["command"] = self.btnProdutosClick
        self.btnProdutos.bind("<Enter>", self.on_enter)
        self.btnProdutos.bind("<Leave>", self.on_leave)
        self.btnProdutos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Pedidos
        self.btnPedidos = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnPedidos["text"] = "Pedidos"
        self.btnPedidos["font"] = self._fontButton
        self.btnPedidos["fg"] = self._bodyTextColor
        self.btnPedidos.bind("<Enter>", self.on_enter)
        self.btnPedidos.bind("<Leave>", self.on_leave)
        self.btnPedidos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Importar
        self.btnImportar = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnImportar["text"] = "Importar dados"
        self.btnImportar["font"] = self._fontButton
        self.btnImportar["fg"] = self._bodyTextColor
        self.btnImportar["command"] = self.btnImportaClick
        self.btnImportar.bind("<Enter>", self.on_enter)
        self.btnImportar.bind("<Leave>", self.on_leave)
        self.btnImportar.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Exportar
        self.btnExportar = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnExportar["text"] = "Exportar dados"
        self.btnExportar["font"] = self._fontButton
        self.btnExportar["fg"] = self._bodyTextColor
        self.btnExportar["command"] = self.btnExportarClick
        self.btnExportar.bind("<Enter>", self.on_enter)
        self.btnExportar.bind("<Leave>", self.on_leave)
        self.btnExportar.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Sobre
        self.btnSobre = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnSobre["text"] = "Sobre" 
        self.btnSobre["font"] = self._fontButton
        self.btnSobre["fg"] = self._bodyTextColor
        self.btnSobre["command"] = self.btnSobreClick
        self.btnSobre.bind("<Enter>", self.on_enter)
        self.btnSobre.bind("<Leave>", self.on_leave)
        self.btnSobre.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Sair
        self.btnSair = Button(self.frameMenu, bg=self._menuColor, borderwidth=0)
        self.btnSair["text"] = "Sair"
        self.btnSair["font"] = self._fontButton
        self.btnSair["fg"] = self._bodyTextColor
        self.btnSair["command"] = self.btnSairClick
        self.btnSair.bind("<Enter>", self.on_enter)
        self.btnSair.bind("<Leave>", self.on_leave)
        self.btnSair.pack(side=TOP, ipady=20, ipadx=60, fill=X)


    #----Animação Botão Sair
    def on_enter(self, event):
        event.widget['background'] = self._buttonHoverColor

    def on_leave(self, event):
        event.widget['background'] = self._menuColor


    #Tela lateral dos Menus principais
    def addFrame(self):
        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

    # Commands dos botões laterias

    def btnUsuariosClick(self):
        self.clientesFrame()

    def btnProdutosClick(self):
        self.produtosFrame()

    def btnAddProdutoClick(self):
        self.addProdutoFrame()    

    def btnImportaClick(self):
        self.importaFrame()

    def btnExportarClick(self):
        self.exportarFrame()

    def btnSobreClick(self):
        self.sobreFrame()

    def btnSairClick(self):
        sys.exit(0)

    # Frames Criados ao Clicar no Botão Lateral

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



        self.frameExpTypes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpTypes.pack(side=LEFT, anchor=N, ipadx=5, padx=45, pady=10)

        expPessoa = ["Ativos", "Inativos"]
        self.expPessoaVar = StringVar()
        for item in expPessoa:
            rdb = Radiobutton(self.frameExpTypes, bg=self._backgroundColor)
            rdb["text"] = item
            rdb["variable"] = self.expPessoaVar
            rdb["value"] = item
            rdb.pack(side=LEFT, anchor=N, ipadx=8)
        self.expPessoaVar.set("Ativos")




        self.frameClientesCommands = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameClientesCommands.pack(side=BOTTOM, fill=X, expand=True, padx=50)
        
        self.btnDeleteCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnDeleteCliente["text"] = "Inativar"
        self.btnDeleteCliente["command"] = self.btnInativaPessoaClick
        self.btnDeleteCliente["font"] = self._fontButton
        self.btnDeleteCliente["fg"] = self._bodyTextColor
        self.btnDeleteCliente.bind("<Enter>", self.on_enter)
        self.btnDeleteCliente.bind("<Leave>", self.on_leave)
        self.btnDeleteCliente.pack(side=RIGHT, ipady=5, ipadx=15)

        self.btnRefreshCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnRefreshCliente["text"] = "Atualizar"
        self.btnRefreshCliente["font"] = self._fontButton
        self.btnRefreshCliente["fg"] = self._bodyTextColor
        self.btnRefreshCliente["command"] = self.btnRefreshClienteClick
        self.btnRefreshCliente.bind("<Enter>", self.on_enter)
        self.btnRefreshCliente.bind("<Leave>", self.on_leave)
        self.btnRefreshCliente.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnUpdateCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnUpdateCliente["text"] = "Alterar"
        self.btnUpdateCliente["font"] = self._fontButton
        self.btnUpdateCliente["fg"] = self._bodyTextColor
        self.btnUpdateCliente["command"] = self.btnUpdateClienteClick
        self.btnUpdateCliente.bind("<Enter>", self.on_enter)
        self.btnUpdateCliente.bind("<Leave>", self.on_leave)
        self.btnUpdateCliente.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnAddCliente = Button(self.frameClientesCommands, bg=self._menuColor, borderwidth=1)
        self.btnAddCliente["text"] = "Adicionar"
        self.btnAddCliente["font"] = self._fontButton
        self.btnAddCliente["fg"] = self._bodyTextColor
        self.btnAddCliente["command"] = self.btnAddClienteClick
        self.btnAddCliente.bind("<Enter>", self.on_enter)
        self.btnAddCliente.bind("<Leave>", self.on_leave)
        self.btnAddCliente.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

    def addClienteFrame(self, cliente=None):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblClientes = Label(self.frameSub, bg=self._backgroundColor)
        self.lblClientes["text"] = "Adicionar Cliente"
        self.lblClientes["font"] = self._fontSubtitle
        self.lblClientes.pack(side=TOP, ipady=20, ipadx=40)

        if cliente != None:
            self.frameClienteId = Frame(self.frameMain, bg=self._backgroundColor)
            self.frameClienteId.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

            self.lblClienteId = Label(self.frameClienteId, bg=self._backgroundColor)
            self.lblClienteId["text"] = "Código"
            self.lblClienteId["font"] = self._fontText
            self.lblClienteId.pack(side=TOP, fill=Y, anchor=W)

            self.entryClienteId = Entry(self.frameClienteId, bg=self._backgroundColor, width=50)
            self.entryClienteId["font"] = self._fontBody
            self.entryClienteId.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.frameDigName = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigName.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigName = Label(self.frameDigName, bg=self._backgroundColor)
        self.lblDigName["text"] = "Nome"
        self.lblDigName["font"] = self._fontText
        self.lblDigName.pack(side=TOP, fill=Y, anchor=W)

        self.entryName = Entry(self.frameDigName, bg=self._backgroundColor, width=50)
        self.entryName["font"] = self._fontBody
        self.entryName.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.frameDigEmail = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigEmail.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigEmail = Label(self.frameDigEmail, bg=self._backgroundColor)
        self.lblDigEmail["text"] = "e-Mail"
        self.lblDigEmail["font"] = self._fontText
        self.lblDigEmail.pack(side=TOP, fill=Y, anchor=W)

        self.entryMail = Entry(self.frameDigEmail, bg=self._backgroundColor, width=50)
        self.entryMail["font"] = self._fontBody
        self.entryMail.pack(side=TOP, anchor=W, padx=15, pady=5)
        
        self.frameDigFone = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigFone.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigFone = Label(self.frameDigFone, bg=self._backgroundColor)
        self.lblDigFone["text"] = "Telefone"
        self.lblDigFone["font"] = self._fontText
        self.lblDigFone.pack(side=TOP, fill=Y, anchor=W)

        self.entryFone = Entry(self.frameDigFone, bg=self._backgroundColor, width=50)
        self.entryFone["font"] = self._fontBody
        self.entryFone.pack(side=TOP, anchor =W, padx=15, pady=5)


        self.frameDigEndereco = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigEndereco.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigEndereco = Label(self.frameDigEndereco, bg=self._backgroundColor)
        self.lblDigEndereco["text"] = "Endereço"
        self.lblDigEndereco["font"] = self._fontText
        self.lblDigEndereco.pack(side=TOP, fill=Y, anchor=W)

        self.entryEndereco = Entry(self.frameDigEndereco, bg=self._backgroundColor,width=50)
        self.entryEndereco["font"] = self._fontBody
        self.entryEndereco.pack(side=TOP, anchor = W, padx=15, pady=5,)

        self.btnAddCliente = Button(self.frameMain, bg=self._menuColor, borderwidth=1)
        self.btnAddCliente["text"] = "Salvar"
        self.btnAddCliente["font"] = self._fontButton
        self.btnAddCliente["fg"] = self._bodyTextColor
        self.btnAddCliente["command"] = self.btnAddClienteBancoClick
        self.btnAddCliente.bind("<Enter>", self.on_enter)
        self.btnAddCliente.bind("<Leave>", self.on_leave)
        self.btnAddCliente.pack(side=LEFT, ipady=5, ipadx=10, padx=10)

        if cliente != None:
            self.entryClienteId.insert(0, cliente[0])
            self.entryClienteId.configure(state='readonly')
            self.entryName.insert(0, cliente[1])
            self.entryMail.insert(0, cliente[2])
            self.entryFone.insert(0, cliente[3])
            self.entryEndereco.insert(0, cliente[4])

    def addProdutoFrame(self, produto=None):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblProdutos = Label(self.frameSub, bg=self._backgroundColor)
        self.lblProdutos["text"] = "Adicionar Produto"
        self.lblProdutos["font"] = self._fontSubtitle
        self.lblProdutos.pack(side=TOP, ipady=20, ipadx=40)

        if produto != None:
            self.frameProdId = Frame(self.frameMain, bg=self._backgroundColor)
            self.frameProdId.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

            self.lblProdId = Label(self.frameProdId, bg=self._backgroundColor)
            self.lblProdId["text"] = "Nome"
            self.lblProdId["font"] = self._fontText
            self.lblProdId.pack(side=TOP, fill=Y, anchor=W)

            self.entryProdId = Entry(self.frameProdId, bg=self._backgroundColor, width=50)
            self.entryProdId["font"] = self._fontBody
            self.entryProdId.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.frameDigNameProd = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigNameProd.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigNameProd = Label(self.frameDigNameProd, bg=self._backgroundColor)
        self.lblDigNameProd["text"] = "Nome"
        self.lblDigNameProd["font"] = self._fontText
        self.lblDigNameProd.pack(side=TOP, fill=Y, anchor=W)

        self.entryNameProd = Entry(self.frameDigNameProd, bg=self._backgroundColor,width=50)
        self.entryNameProd["font"] = self._fontBody
        self.entryNameProd.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.frameDigDescricao = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigDescricao.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigDescricao = Label(self.frameDigDescricao, bg=self._backgroundColor)
        self.lblDigDescricao["text"] = "Descrição"
        self.lblDigDescricao["font"] = self._fontText
        self.lblDigDescricao.pack(side=TOP, fill=Y, anchor=W)

        self.entryDescricao = Entry(self.frameDigDescricao, bg=self._backgroundColor,width=50)
        self.entryDescricao["font"] = self._fontBody
        self.entryDescricao.pack(side=TOP, anchor=W, padx=15, pady=5)
        
        self.frameDigQuant = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigQuant.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigQuant = Label(self.frameDigQuant, bg=self._backgroundColor)
        self.lblDigQuant["text"] = "Quantidade"
        self.lblDigQuant["font"] = self._fontText
        self.lblDigQuant.pack(side=TOP, fill=Y, anchor=W)

        self.entryQuant = Entry(self.frameDigQuant, bg=self._backgroundColor,width=50)
        self.entryQuant["font"] = self._fontBody
        self.entryQuant.pack(side=TOP, anchor =W, padx=15, pady=5)

        self.frameDigPreco = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDigPreco.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblDigPreco = Label(self.frameDigPreco, bg=self._backgroundColor)
        self.lblDigPreco["text"] = "Preço"
        self.lblDigPreco["font"] = self._fontText
        self.lblDigPreco.pack(side=TOP, fill=Y, anchor=W)

        self.entryPreco = Entry(self.frameDigPreco, bg=self._backgroundColor,width=50)
        self.entryPreco["font"] = self._fontBody
        self.entryPreco.pack(side=TOP, anchor = W, padx=15, pady=5,)

        self.btnAddProduto = Button(self.frameMain, bg=self._menuColor, borderwidth=1)
        self.btnAddProduto["text"] = "Salvar"
        self.btnAddProduto["font"] = self._fontButton
        self.btnAddProduto["fg"] = self._bodyTextColor
        self.btnAddProduto["command"] = self.btnAddProdutoBancoClick
        self.btnAddProduto.bind("<Enter>", self.on_enter)
        self.btnAddProduto.bind("<Leave>", self.on_leave)
        self.btnAddProduto.pack(side=LEFT, ipady=5, ipadx=10, padx=10)

        if produto != None:
            self.entryProdId.insert(0, produto[0])
            self.entryNameProd.insert(0, produto[1])
            self.entryDescricao.insert(0, produto[2])
            self.entryQuant.insert(0, produto[3])
            self.entryPreco.insert(0, produto[4])
            self.entryProdId.configure(state='readonly')

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
        self.btnDeleteProduto["fg"] = self._bodyTextColor
        self.btnDeleteProduto.bind("<Enter>", self.on_enter)
        self.btnDeleteProduto.bind("<Leave>", self.on_leave)
        self.btnDeleteProduto.pack(side=RIGHT, ipady=5, ipadx=10)

        self.btnUpdateProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnUpdateProduto["text"] = "Alterar"
        self.btnUpdateProduto["font"] = self._fontButton
        self.btnUpdateProduto["fg"] = self._bodyTextColor
        self.btnUpdateProduto["command"] = self.btnUpdateProdutoClick
        self.btnUpdateProduto.bind("<Enter>", self.on_enter)
        self.btnUpdateProduto.bind("<Leave>", self.on_leave)
        self.btnUpdateProduto.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnAddProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnAddProduto["text"] = "Adicionar"
        self.btnAddProduto["font"] = self._fontButton
        self.btnAddProduto["fg"] = self._bodyTextColor
        self.btnAddProduto["command"] = self.btnAddProdutoClick
        self.btnAddProduto.bind("<Enter>", self.on_enter)
        self.btnAddProduto.bind("<Leave>", self.on_leave)
        self.btnAddProduto.pack(side=RIGHT, ipady=5, ipadx=10)
   
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

        self.frameImpUrl = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameImpUrl.pack(anchor=N, fill=BOTH, padx=60, ipadx=60, pady=35)

        self.lblImpUrl = Label(self.frameImpUrl, bg=self._backgroundColor)
        self.lblImpUrl["text"] = "Endereço dos dados"
        self.lblImpUrl["font"] = self._fontText
        self.lblImpUrl.pack(side=TOP, fill=Y, anchor=W)

        self.entryImpUrl = Entry(self.frameImpUrl, bg=self._backgroundColor)
        self.entryImpUrl["font"] = self._fontBody
        self.entryImpUrl.pack(side=TOP, fill=X, padx=15, pady=5)

        self.frameImportar = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameImportar.pack(side=TOP, fill=Y, anchor=W, ipadx=60, padx=60)

        self.lblImpTudo = Label(self.frameImportar, bg=self._backgroundColor)
        self.lblImpTudo["text"] = "Exportar dados"
        self.lblImpTudo["font"] = self._fontText
        self.lblImpTudo["justify"] = LEFT
        self.lblImpTudo.pack(side=TOP, anchor=W, pady=5)

        self.lblImportarTudo = Label(self.frameImportar, bg=self._backgroundColor)
        self.lblImportarTudo["justify"] = LEFT
        self.lblImportarTudo["font"] = self._fontBody
        self.lblImportarTudo["text"] = "Exporta os dados armazenados no sistema em um arquivo no formato JSON, que pode possui o conteúdo\ndas tabelas Pessoa, Produto, Pedido ou ItemPedido, além de possibilitar a exportação de todos os dados."
        self.lblImportarTudo.pack(side=TOP, fill=Y, anchor=W, ipadx=10)

        self.frameImpTypes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameImpTypes.pack(side=TOP, fill=Y, anchor=N, ipadx=60, padx=60, pady=10)

        impTypes = ["Tudo", "Pessoas", "Produtos", "Pedidos", "ItensPedidos"]
        self.impTypeVar = StringVar()
        for item in impTypes:
            rdb = Radiobutton(self.frameImpTypes, bg=self._backgroundColor)
            rdb["text"] = item
            rdb["variable"] = self.impTypeVar
            rdb["value"] = item
            rdb.pack(side=LEFT, anchor=N, ipadx=8)
        self.impTypeVar.set("Tudo")

        self.btnImportarDados = Button(self.frameMain, bg=self._backgroundColor)
        self.btnImportarDados["text"] = "Importar"
        self.btnImportarDados["font"] = self._fontButton
        self.btnImportarDados["fg"] = self._bodyTextColor
        self.btnImportarDados["command"] = self.btnImportarDadosClick
        self.btnImportarDados.bind("<Enter>", self.on_enter)
        self.btnImportarDados.bind("<Leave>", self.on_leave)
        self.btnImportarDados.pack(side=TOP, fill=Y, anchor=N, padx=60, ipady=5, ipadx=15)

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
        self.entryExpName["font"] = self._fontBody
        self.entryExpName.insert(0, "backup")
        self.entryExpName.pack(side=TOP, fill=X, padx=15, pady=5)

        self.frameExpPath = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpPath.pack(anchor=N, fill=BOTH, padx=60, ipadx=60, pady=35)

        self.lblExpPath = Label(self.frameExpPath, bg=self._backgroundColor)
        self.lblExpPath["text"] = "Caminho para exportar os dados"
        self.lblExpPath["font"] = self._fontText
        self.lblExpPath.pack(side=TOP, fill=Y, anchor=W)

        self.entryExpPath = Entry(self.frameExpPath, bg=self._backgroundColor)
        self.entryExpPath["font"] = self._fontBody
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
        self.lblExportarTudo["font"] = self._fontBody
        self.lblExportarTudo["text"] = "Exporta os dados armazenados no sistema em um arquivo no formato JSON, que pode possui o conteúdo\ndas tabelas Pessoa, Produto, Pedido ou ItemPedido, além de possibilitar a exportação de todos os dados."
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
        self.btnExportarDados["font"] = self._fontButton
        self.btnExportarDados["fg"] = self._bodyTextColor
        self.btnExportarDados["command"] = self.btnExportarDadosClick
        self.btnExportarDados.bind("<Enter>", self.on_enter)
        self.btnExportarDados.bind("<Leave>", self.on_leave)
        self.btnExportarDados.pack(side=TOP, fill=Y, anchor=N, padx=60, ipady=5, ipadx=15)

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
        self.lblTemaInfo["font"] = self._fontBody
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
        self.lblAppInfo["font"] = self._fontBody
        self.lblAppInfo["text"] = "O prosósito da aplicação é auxiliar o controle e gerenciamento de um estabelecimento que possua o intuito de\ncomercializar produtos como ração e acessórios para animais."
        self.lblAppInfo.pack(side=TOP, ipadx=10)

        self.frameDevs = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameDevs.pack(side=TOP, fill=Y, anchor=W, ipadx=60)

        self.lblDevs = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDevs["text"] = "Desenvolvedores"
        self.lblDevs["font"] = self._fontText
        self.lblDevs.pack(side=TOP, anchor=W, ipadx=60, pady=5)

        self.lblDev1 = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDev1["justify"] = LEFT
        self.lblDev1["font"] = self._fontBody
        self.lblDev1["text"] = "%-25s RA: %-14s" %("Fernando Marchetti", "2840481523011")
        self.lblDev1.pack(side=TOP, ipadx=10)

        self.lblDev2 = Label(self.frameDevs, bg=self._backgroundColor)
        self.lblDev2["justify"] = LEFT
        self.lblDev2["font"] = self._fontBody
        self.lblDev2["text"] = "%-25s  RA: %-14s" %("Vitor Xavier de Souza", "2840481523039")
        self.lblDev2.pack(side=TOP, ipadx=10)

        self.frameGit = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameGit.pack(side=TOP, fill=Y, expand=True, anchor=W, pady=35)

        self.lblGit = Label(self.frameGit, bg=self._backgroundColor)
        self.lblGit["text"] = "Repositório do projeto"
        self.lblGit["font"] = self._fontText
        self.lblGit.pack(side=TOP, anchor=W, ipadx=60, pady=5)

        self.entryGit = Entry(self.frameGit, bg=self._backgroundColor, width=40, borderwidth=0)
        self.entryGit["font"] = self._fontBody
        self.entryGit["readonlybackground"] = self._backgroundColor
        self.entryGit.insert(0, "https://github.com/Vitor-Xavier/ProjetoPetshop")
        self.entryGit.configure(state='readonly')
        self.entryGit.pack(side=TOP, fill=BOTH, anchor=W, ipadx=60, pady=5, padx=70)

    # Funcinalidades dentro dos Frames
    
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

    def btnImportarDadosClick(self):
        if (self.impTypeVar.get() == "Tudo"):
            importExport.importarBanco(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Pessoas"):
            importExport.importarPessoas(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Produtos"):
            importExport.importarProdutos(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Pedidos"):
            importExport.importarPedidos(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "ItensPedidos"):
            importExport.importarItensPedidos(self.entryImpUrl.get())


    # def btnUpdateClienteClick(self):
    #     cod = self.getSelectedPessoa()
    #     print("Id: " + str(cod))

    def btnUpdateProdutoClick(self):
        cod = self.getSelectedProduto()
        produto = connect.selectProduto(cod)
        self.addProdutoFrame(produto)

    def btnUpdateClienteClick(self):
        cod = self.getSelectedPessoa()
        pessoa = connect.selectPessoa(cod)
        self.addClienteFrame(pessoa)

    def btnRefreshClienteClick(self):
        self.carregaClientes((self.expPessoaVar.get() == "Ativos"))
        # cod = self.getSelectedPessoa()
        # print("Id: " + str(cod))

    def btnAddClienteClick(self):
        self.addClienteFrame()

    def btnAddClienteBancoClick(self):
        pessoa = models.Pessoa()
        pessoa.nome = self.entryName.get()
        pessoa.email = self.entryMail.get()
        pessoa.telefone = self.entryFone.get()
        pessoa.endereco = self.entryEndereco.get()

        if (self.entryClienteId.winfo_exists()):
            pessoa.pessoa_id = self.entryClienteId.get()
            connect.updatePessoa(pessoa)
        else:
            connect.insertPessoa(pessoa)
        self.clientesFrame()

    def btnAddProdutoBancoClick(self):
        produto = models.Produto()
        produto.nome = self.entryNameProd.get()
        produto.descricao = self.entryDescricao.get()
        produto.quantidade = self.entryQuant.get()
        produto.preco = self.entryPreco.get()

        if (self.entryProdId.winfo_exists()):
            produto.produto_id = self.entryProdId.get()
            connect.updateProduto(produto)
        else:
            connect.insertProduto(produto)
        self.produtosFrame()       
    
    def getSelectedPessoa(self):
        pos = self.listClientes.curselection()
        item = self.listClientes.get(pos)
        return int(item[3:7])

    def getSelectedProduto(self):
        pos = self.listProdutos.curselection()
        item = self.listProdutos.get(pos)
        return int(item[3:7])

    # Atualiza listas

    def carregaClientes(self, onlyAtivos=True):
        clientes = connect.selectPessoas(onlyAtivos)
        self.listClientes.delete(0, END)
        for item in clientes:
            self.listClientes.insert(END, "Id: %-4d Nome: %-30s Email: %-25s Telefone: %-16s Endereco: %-40s" %(item[0], item[1], item[2], item[3], item[4]))

    def carregaProdutos(self, onlyAtivos=True):
        produtos = connect.selectProdutos(onlyAtivos)
        self.listProdutos.delete(0, END)
        for item in produtos:
            self.listProdutos.insert(END, "Id: %-4d Nome: %-30s Descrição: %-40s Quantidade: %-8s Preço: %-10s" %(item[0], item[1], item[2], item[3], item[4]))

def main():
    app = FramePrincipal()
    app.mainloop()

main()