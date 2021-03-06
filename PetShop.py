import sys
import connect
import models
import importExport
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
import json
import os
import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
    def __init__(self, master=None, user=None):
        super().__init__()
        self.master.title(self._title)
        self.master.resizable(True, True)
        self.master.iconbitmap("res/icon.ico")
        self.master["bg"] = self._backgroundColor
        self.centralizar(1000, 600) # Resolução da tela principal
        self.pack()
        self.addTitle("Menu")
        self.addMenu()
        self.addFrame()

        self.loggedUser = user

        self.btnInicioClick()

    def centralizar(self, largura, altura):
        px = int((self.master.winfo_screenwidth() - largura) / 2)
        py = int((self.master.winfo_screenheight() - altura) / 2)
        self.master.geometry("{}x{}+{}+{}".format(largura, altura, px, py))

    def exibirMensagem(self, msg):
        mbox.showinfo("Pet Shop", msg) 

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

        #Botão inicio
        self.btnInicio = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnInicio["text"] = "Início"
        self.btnInicio["font"] = self._fontButton
        self.btnInicio["fg"] = self._bodyTextColor
        self.btnInicio["command"] = self.btnInicioClick
        self.btnInicio.bind("<Enter>", self.on_enter)
        self.btnInicio.bind("<Leave>", self.on_leave)
        self.btnInicio.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Novo Pedido
        self.btnPedidos = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnPedidos["text"] = "Novo Pedido"
        self.btnPedidos["font"] = self._fontButton
        self.btnPedidos["fg"] = self._bodyTextColor
        self.btnPedidos["command"] = self.btnNovoPedidoClick
        self.btnPedidos.bind("<Enter>", self.on_enter)
        self.btnPedidos.bind("<Leave>", self.on_leave)
        self.btnPedidos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

        #Botão Pedidos
        self.btnPedidos = Button(self.frameMenu, bg=self._menuColor,borderwidth=0)
        self.btnPedidos["text"] = "Pedidos"
        self.btnPedidos["font"] = self._fontButton
        self.btnPedidos["fg"] = self._bodyTextColor
        self.btnPedidos["command"] = self.btnPedidoClick
        self.btnPedidos.bind("<Enter>", self.on_enter)
        self.btnPedidos.bind("<Leave>", self.on_leave)
        self.btnPedidos.pack(side=TOP, ipady=20, ipadx=60, fill=X)

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


    #----Animação dos Botões
    def on_enter(self, event):
        event.widget['background'] = self._buttonHoverColor

    def on_leave(self, event):
        event.widget['background'] = self._menuColor


    #Tela lateral dos Menus principais
    def addFrame(self):
        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)


    # Commands dos botões laterias

    def btnInicioClick(self):
        self.homeFrame()

    def btnUsuariosClick(self):
        self.clientesFrame()

    def btnProdutosClick(self):
        self.produtosFrame()

    def btnAddProdutoClick(self):
        self.addProdutoFrame()    

    def btnPedidoClick(self):
        self.pedidoFrame()

    def btnNovoPedidoClick(self):
        self.addPedidoFrame()

    def btnImportaClick(self):
        self.importaFrame()

    def btnExportarClick(self):
        self.exportarFrame()

    def btnSobreClick(self):
        self.sobreFrame()

    def btnSairClick(self):
        sys.exit(0)

    # Frames Criados ao Clicar no Botão Lateral

    def homeFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblHome = Label(self.frameSub, bg=self._backgroundColor)
        self.lblHome["text"] = "Início"
        self.lblHome["font"] = self._fontSubtitle
        self.lblHome.pack(side=TOP, ipady=20, ipadx=40)

        self.frameVendas = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameVendas.pack(side=LEFT, anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        data = connect.selectVendas()
        datas = [var[0] for var in data]
        vendas = [var[1] for var in data]

        f = Figure(figsize=(3,5), dpi=100)
        a = f.add_subplot(111)
        a.set_title('Vendas na última semana')
        a.plot(datas,vendas)
        a.set_xlabel('Datas')
        a.set_ylabel('Valor de vendas em Reais (R$)')

        self.canvas = FigureCanvasTkAgg(f, self.frameVendas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        self.frameListas = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameListas.pack(side=LEFT, anchor=N, fill=BOTH, expand=True, padx=40)

        self.frameEstoque = Frame(self.frameListas, bg=self._backgroundColor)
        self.frameEstoque.pack(side=TOP, anchor=N, fill=BOTH, pady=50)

        self.lblEstoque = Label(self.frameEstoque, bg=self._backgroundColor)
        self.lblEstoque["text"] = "Estoque baixo (menos de 10 itens)"
        self.lblEstoque["font"] = self._fontText
        self.lblEstoque.pack(side=TOP)

        scrollY = Scrollbar(self.frameEstoque, orient=VERTICAL)

        self.listEstoque = Listbox(self.frameEstoque, yscrollcommand=scrollY.set)
        self.listEstoque["height"] = 5
        self.listEstoque["selectmode"] = SINGLE

        self.carregaEstoque()

        self.listEstoque.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listEstoque.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.frameUltVendas = Frame(self.frameListas, bg=self._backgroundColor)
        self.frameUltVendas.pack(side=TOP, anchor=N, fill=BOTH)

        self.lblEstoque = Label(self.frameUltVendas, bg=self._backgroundColor)
        self.lblEstoque["text"] = "Últimas vendas"
        self.lblEstoque["font"] = self._fontText
        self.lblEstoque.pack(side=TOP)

        scrollY = Scrollbar(self.frameUltVendas, orient=VERTICAL)

        self.listVendas = Listbox(self.frameUltVendas, yscrollcommand=scrollY.set)
        self.listVendas["height"] = 5
        self.listVendas["selectmode"] = SINGLE

        self.carregaVendas()

        self.listVendas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listVendas.yview
        scrollY.pack(side=LEFT, fill=Y)

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
            rdb["command"] = self.onRadioStatusClienteSelect
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
        self.btnDeleteCliente.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

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

        self.entryClienteId.insert(0, "0")
        if cliente != None:
            self.entryClienteId.delete(0, END)
            self.entryClienteId.insert(0, cliente[0])
            self.entryName.insert(0, cliente[1])
            self.entryMail.insert(0, cliente[2])
            self.entryFone.insert(0, cliente[3])
            self.entryEndereco.insert(0, cliente[4])
        self.entryClienteId.configure(state='readonly')

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

        self.frameProdId = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdId.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblProdId = Label(self.frameProdId, bg=self._backgroundColor)
        self.lblProdId["text"] = "Código"
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

        self.entryProdId.insert(0, "0")
        if produto != None:
            self.entryProdId.delete(0, END)
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


        self.frameExpTypes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpTypes.pack(side=LEFT, anchor=N, ipadx=5, padx=45, pady=10)

        expProd = ["Ativos", "Inativos"]
        self.expProdVar = StringVar()
        for item in expProd:
            rdb = Radiobutton(self.frameExpTypes, bg=self._backgroundColor)
            rdb["text"] = item
            rdb["variable"] = self.expProdVar
            rdb["command"] = self.onRadioStatusProdutoSelect
            rdb["value"] = item
            rdb.pack(side=LEFT, anchor=N, ipadx=8)
        self.expProdVar.set("Ativos")


        self.frameProdutosCommands = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdutosCommands.pack(side=BOTTOM, fill=X, expand=True, padx=50)

        
        self.btnDeleteProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnDeleteProduto["text"] = "Inativar"
        self.btnDeleteProduto["command"] = self.btnInativaProdutoClick
        self.btnDeleteProduto["font"] = self._fontButton
        self.btnDeleteProduto["fg"] = self._bodyTextColor
        self.btnDeleteProduto.bind("<Enter>", self.on_enter)
        self.btnDeleteProduto.bind("<Leave>", self.on_leave)
        self.btnDeleteProduto.pack(side=RIGHT, ipady=5, ipadx=10)

        self.btnRefreshProduto = Button(self.frameProdutosCommands, bg=self._menuColor, borderwidth=1)
        self.btnRefreshProduto["text"] = "Atualizar"
        self.btnRefreshProduto["font"] = self._fontButton
        self.btnRefreshProduto["fg"] = self._bodyTextColor
        self.btnRefreshProduto["command"] = self.btnRefreshProdutoClick
        self.btnRefreshProduto.bind("<Enter>", self.on_enter)
        self.btnRefreshProduto.bind("<Leave>", self.on_leave)
        self.btnRefreshProduto.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

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

    def dadosImportadosFrame(self, imported, importedtype):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblimporta = Label(self.frameSub, bg=self._backgroundColor)
        self.lblimporta["text"] = "Importar dados para Json"
        self.lblimporta["font"] = self._fontSubtitle
        self.lblimporta.pack(side=TOP, ipady=20, ipadx=40)

        self.frameImportados = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameImportados.pack(anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        scrollY = Scrollbar(self.frameImportados, orient=VERTICAL)

        self.listImportados = Listbox(self.frameImportados, yscrollcommand=scrollY.set)
        self.listImportados["height"] = 16
        self.listImportados["selectmode"] = SINGLE

        self.listImportados.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listImportados.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.carregaImportados(imported, importedtype)

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

    def pedidoFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblPedidos = Label(self.frameSub, bg=self._backgroundColor)
        self.lblPedidos["text"] = "Pedidos de Venda"
        self.lblPedidos["font"] = self._fontSubtitle
        self.lblPedidos.pack(side=TOP, ipady=20, ipadx=40)

        self.framePedidos = Frame(self.frameMain, bg=self._backgroundColor)
        self.framePedidos.pack(anchor=N, fill=BOTH, expand=True, padx=50, pady=30)

        scrollY = Scrollbar(self.framePedidos, orient=VERTICAL)

        self.listPedidos = Listbox(self.framePedidos, yscrollcommand=scrollY.set)
        self.listPedidos["height"] = 10
        self.listPedidos["selectmode"] = SINGLE
        self.listPedidos.bind("<<ListboxSelect>>", self.onPedidoSelected)

        self.listPedidos.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listPedidos.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.carregaPedidos()

        self.frameExpTypes = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameExpTypes.pack(side=LEFT, anchor=N, ipadx=5, padx=45, pady=10)
        
    def addPedidoFrame(self):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblPedido = Label(self.frameSub, bg=self._backgroundColor)
        self.lblPedido["text"] = "Novo pedido"
        self.lblPedido["font"] = self._fontSubtitle
        self.lblPedido.pack(side=TOP, ipady=20, ipadx=40)

        self.framePedido = Frame(self.frameMain, bg=self._backgroundColor)
        self.framePedido.pack(anchor=N, fill=BOTH, padx=60, ipadx=60, pady=10)

        self.framePedidoId = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedidoId.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedidoId = Label(self.framePedidoId, bg=self._backgroundColor)
        self.lblPedidoId["text"] = "Código"
        self.lblPedidoId["font"] = self._fontText
        self.lblPedidoId.pack(side=TOP, fill=Y, anchor=W)

        self.entryPedidoId = Entry(self.framePedidoId, bg=self._backgroundColor, width=20)
        self.entryPedidoId["font"] = self._fontBody
        self.entryPedidoId.pack(side=TOP, anchor=W, padx=15, pady=5)

        pedidoId, data_pedido = self.novoPedido()

        self.entryPedidoId.insert(0, pedidoId)
        self.entryPedidoId.configure(state='readonly')

        self.framePedCliente = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedCliente.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedCliente = Label(self.framePedCliente, bg=self._backgroundColor)
        self.lblPedCliente["text"] = "Cliente"
        self.lblPedCliente["font"] = self._fontText
        self.lblPedCliente.pack(side=TOP, fill=Y, anchor=W)

        clientes = self.carregaBoxClientes()
        self.cliente_value = StringVar()
        self.comboCliente = ttk.Combobox(self.framePedCliente, textvariable=self.cliente_value, values=clientes, state='readonly')
        self.comboCliente.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.framePedidoData = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedidoData.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedidoData = Label(self.framePedidoData, bg=self._backgroundColor)
        self.lblPedidoData["text"] = "Data"
        self.lblPedidoData["font"] = self._fontText
        self.lblPedidoData.pack(side=TOP, fill=Y, anchor=W)

        self.entryPedidoData = Entry(self.framePedidoData, bg=self._backgroundColor,width=50)
        self.entryPedidoData["font"] = self._fontBody
        self.entryPedidoData.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.entryPedidoData.insert(0, data_pedido)
        self.entryPedidoData.configure(state='readonly')
        
        self.framePedQtd = Frame(self.frameMain, bg=self._backgroundColor, width=50)
        self.framePedQtd.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblPedQtd = Label(self.framePedQtd, bg=self._backgroundColor)
        self.lblPedQtd["text"] = "Quantidade"
        self.lblPedQtd["font"] = self._fontText
        self.lblPedQtd.pack(side=TOP, fill=Y, anchor=W)

        self.entryPedQtd = Entry(self.framePedQtd, bg=self._backgroundColor,width=20)
        self.entryPedQtd["font"] = self._fontBody
        self.entryPedQtd.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.entryPedQtd.insert(0, "1")

        self.frameTotal = Frame(self.frameMain, bg=self._backgroundColor, width=50)
        self.frameTotal.pack(anchor=N, fill=BOTH, padx=60, ipadx=60)

        self.lblTotal = Label(self.frameTotal, bg=self._backgroundColor)
        self.lblTotal["text"] = "Valor Total"
        self.lblTotal["font"] = self._fontText
        self.lblTotal.pack(side=TOP, fill=Y, anchor=W)

        self.entryValorTotal = Entry(self.frameTotal, bg=self._backgroundColor,width=20)
        self.entryValorTotal["font"] = self._fontBody
        self.entryValorTotal.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.entryValorTotal.insert(0, "R$: 0.00")
        self.entryValorTotal.configure(state='readonly')

        self.frameProdItens = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdItens.pack(anchor=N, fill=BOTH, padx=50, pady=15)

        self.frameProdutos = Frame(self.frameProdItens, bg=self._backgroundColor)
        self.frameProdutos.pack(side=LEFT, anchor=N, fill=BOTH, padx=10, expand=True)

        scrollY = Scrollbar(self.frameProdutos, orient=VERTICAL)

        self.listPedProdutos = Listbox(self.frameProdutos, yscrollcommand=scrollY.set)
        self.listPedProdutos["height"] = 8
        self.listPedProdutos["selectmode"] = SINGLE

        self.carregaPedProdutos()
        #self.listProdutos.bind("<<ListboxSelect>>", self.onProdutoSelected)

        self.listPedProdutos.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY["command"] = self.listPedProdutos.yview
        scrollY.pack(side=LEFT, fill=Y)

        self.frameItens = Frame(self.frameProdItens, bg=self._backgroundColor)
        self.frameItens.pack(side=LEFT, anchor=N, fill=BOTH, padx=10, expand=True)

        scrollY2 = Scrollbar(self.frameItens, orient=VERTICAL)

        self.listItens = Listbox(self.frameItens, yscrollcommand=scrollY2.set)
        self.listItens["height"] = 8
        self.listItens["selectmode"] = SINGLE

        self.carregaItens()

        self.listItens.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY2["command"] = self.listItens.yview
        scrollY2.pack(side=LEFT, fill=Y)

        self.frameButtons = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameButtons.pack(side=BOTTOM, anchor=N, fill=BOTH, padx=50, expand=True)

        self.btnAddItemPedido = Button(self.frameButtons, bg=self._menuColor, borderwidth=1)
        self.btnAddItemPedido["text"] = "Adicionar"
        self.btnAddItemPedido["font"] = self._fontButton
        self.btnAddItemPedido["fg"] = self._bodyTextColor
        self.btnAddItemPedido["command"] = self.btnAddItemClick
        self.btnAddItemPedido.bind("<Enter>", self.on_enter)
        self.btnAddItemPedido.bind("<Leave>", self.on_leave)
        self.btnAddItemPedido.pack(side=LEFT, ipady=5, ipadx=10, padx=10)
        
        self.btnFinalizaPedido = Button(self.frameButtons, bg=self._menuColor, borderwidth=1)
        self.btnFinalizaPedido["text"] = "Finalizar"
        self.btnFinalizaPedido["font"] = self._fontButton
        self.btnFinalizaPedido["fg"] = self._bodyTextColor
        self.btnFinalizaPedido["command"] = self.btnFinalizaPedidoClick
        self.btnFinalizaPedido.bind("<Enter>", self.on_enter)
        self.btnFinalizaPedido.bind("<Leave>", self.on_leave)
        self.btnFinalizaPedido.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

        self.btnRemoveItemPedido = Button(self.frameButtons, bg=self._menuColor, borderwidth=1)
        self.btnRemoveItemPedido["text"] = "Remover"
        self.btnRemoveItemPedido["font"] = self._fontButton
        self.btnRemoveItemPedido["fg"] = self._bodyTextColor
        self.btnRemoveItemPedido["command"] = self.btnRemoveItemClick
        self.btnRemoveItemPedido.bind("<Enter>", self.on_enter)
        self.btnRemoveItemPedido.bind("<Leave>", self.on_leave)
        self.btnRemoveItemPedido.pack(side=RIGHT, ipady=5, ipadx=10, padx=10)

    def sobrePedidoFrame(self, pedido):
        self.frameMain.destroy()

        self.frameMain = Frame(bg=self._backgroundColor)
        self.frameMain.pack(side=RIGHT, fill=BOTH, expand=True)

        self.frameSub = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameSub.pack(side=TOP, fill=Y, anchor=W)

        self.lblPedido = Label(self.frameSub, bg=self._backgroundColor)
        self.lblPedido["text"] = "Pedido"
        self.lblPedido["font"] = self._fontSubtitle
        self.lblPedido.pack(side=TOP, ipady=20, ipadx=40)

        self.framePedido = Frame(self.frameMain, bg=self._backgroundColor)
        self.framePedido.pack(anchor=N, fill=BOTH, padx=60, ipadx=60, pady=10)

        self.framePedidoId = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedidoId.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedidoId = Label(self.framePedidoId, bg=self._backgroundColor)
        self.lblPedidoId["text"] = "Código"
        self.lblPedidoId["font"] = self._fontText
        self.lblPedidoId.pack(side=TOP, fill=Y, anchor=W)

        self.entryPedidoId = Entry(self.framePedidoId, bg=self._backgroundColor, width=20)
        self.entryPedidoId["font"] = self._fontBody
        self.entryPedidoId.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.framePedCliente = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedCliente.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedCliente = Label(self.framePedCliente, bg=self._backgroundColor)
        self.lblPedCliente["text"] = "Cliente"
        self.lblPedCliente["font"] = self._fontText
        self.lblPedCliente.pack(side=TOP, fill=Y, anchor=W)
        
        cliente = connect.selectPessoa(pedido[2])

        clientes = []
        clientes.append("%-4s - %-30s" %(cliente[0], cliente[1]))

        self.cliente_value = StringVar()
        self.comboCliente = ttk.Combobox(self.framePedCliente, textvariable=self.cliente_value, values=clientes, state='readonly')
        self.comboCliente.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.framePedidoData = Frame(self.framePedido, bg=self._backgroundColor, width=40)
        self.framePedidoData.pack(side=LEFT, anchor=N, fill=BOTH)

        self.lblPedidoData = Label(self.framePedidoData, bg=self._backgroundColor)
        self.lblPedidoData["text"] = "Data"
        self.lblPedidoData["font"] = self._fontText
        self.lblPedidoData.pack(side=TOP, fill=Y, anchor=W)

        self.entryPedidoData = Entry(self.framePedidoData, bg=self._backgroundColor,width=50)
        self.entryPedidoData["font"] = self._fontBody
        self.entryPedidoData.pack(side=TOP, anchor=W, padx=15, pady=5)

        self.frameProdItens = Frame(self.frameMain, bg=self._backgroundColor)
        self.frameProdItens.pack(anchor=N, fill=BOTH, padx=50, pady=15)

        self.frameItens = Frame(self.frameProdItens, bg=self._backgroundColor)
        self.frameItens.pack(side=LEFT, anchor=N, fill=BOTH, padx=10, expand=True)

        scrollY2 = Scrollbar(self.frameItens, orient=VERTICAL)

        self.listItens = Listbox(self.frameItens, yscrollcommand=scrollY2.set)
        self.listItens["height"] = 8
        self.listItens["selectmode"] = SINGLE 

        self.listItens.pack(side=LEFT, fill=BOTH, expand=True)
        scrollY2["command"] = self.listItens.yview
        scrollY2.pack(side=LEFT, fill=Y)

        self.entryPedidoId.insert(0, pedido[0])
        self.entryPedidoId.configure(state='readonly')

        self.entryPedidoData.insert(0, pedido[3])
        self.entryPedidoData.configure(state='readonly')

        self.comboCliente.current(0)

        self.carregaItens()

    # Funcinalidades dentro dos Frames
    
    def btnInativaProdutoClick(self):
        cod = self.getSelectedProduto()
        connect.altStatusProduto(cod, self.expProdVar.get() != "Ativos")
        self.carregaProdutos(self.expProdVar.get() == "Ativos")

    def btnInativaPessoaClick(self):
        cod = self.getSelectedPessoa()
        connect.altStatusPessoa(cod, self.expPessoaVar.get() != "Ativos")
        self.carregaClientes(self.expPessoaVar.get() == "Ativos")

    def onPedidoSelected(self, event):
        pos = self.listPedidos.curselection()
        item = self.listPedidos.get(pos)
        pedidoId = int(item[3:7])
        pedido = connect.selectPedido(pedidoId)
        self.sobrePedidoFrame(pedido)

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
            dados = importExport.importarBanco(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Pessoas"):
            dados = importExport.importarPessoas(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Produtos"):
            dados = importExport.importarProdutos(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "Pedidos"):
            dados = importExport.importarPedidos(self.entryImpUrl.get())
        elif (self.impTypeVar.get() == "ItensPedidos"):
            dados = importExport.importarItensPedidos(self.entryImpUrl.get())
        self.dadosImportadosFrame(dados, self.impTypeVar.get()) 
        
    def btnUpdateProdutoClick(self):
        cod = self.getSelectedProduto()
        produto = connect.selectProduto(cod)
        self.addProdutoFrame(produto)

    def btnRefreshProdutoClick(self):
        self.carregaProdutos((self.expProdVar.get() == "Ativos"))

    def btnUpdateClienteClick(self):
        cod = self.getSelectedPessoa()
        pessoa = connect.selectPessoa(cod)
        self.addClienteFrame(pessoa)

    def btnRefreshClienteClick(self):
        self.carregaClientes((self.expPessoaVar.get() == "Ativos"))
        # cod = self.getSelectedPessoa()
        # print("Id: " + str(cod))

    def btnFinalizaPedidoClick(self):
        try:
            pedidoId = int(self.entryPedidoId.get())
            clienteId = str(self.getSelectPedCliente())
            connect.updatePedidoCliente(pedidoId, clienteId)
            self.pedidoFrame()
        except Exception:
            self.exibirMensagem("Nenhum cliente selecionado")

    def btnAddClienteClick(self):
        self.addClienteFrame()

    def btnAddItemClick(self):
        item = models.ItemPedido()
        item.pedido_id = int(self.entryPedidoId.get())
        item.produto_id = self.getSelectedPedProduto()
        item.quantidade = int(self.entryPedQtd.get())
        item.preco_unitario = connect.selectProduto(item.produto_id)[4]
        prodQtd = connect.selectProduto(item.produto_id)[3]
        if (prodQtd - item.quantidade) >= 0:
            connect.insertItemPedido(item)
            connect.updateProdutoQtd(item.produto_id, item.quantidade * -1)
            self.carregaItens()
            self.carregaPedProdutos()
            self.atualizaTotalPedido()
        else:
            self.exibirMensagem("Quantidade superior ao disponivel em estoque")

    def btnRemoveItemClick(self):
        quantidade = int(self.entryPedQtd.get())
        produtoId, pedidoId = self.getSelectedItemProduto()
        connect.inativaItemPedido(pedidoId, produtoId)
        connect.updateProdutoQtd(produtoId, quantidade)
        self.carregaItens()
        self.carregaPedProdutos()
        self.atualizaTotalPedido()
        
    def btnAddClienteBancoClick(self):
        pessoa = models.Pessoa()
        pessoa.nome = self.entryName.get()
        pessoa.email = self.entryMail.get()
        pessoa.telefone = self.entryFone.get()
        pessoa.endereco = self.entryEndereco.get()


        if (self.entryClienteId.get() != "0"):
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

        if (self.entryProdId.get() != "0"):
            produto.produto_id = self.entryProdId.get()
            connect.updateProduto(produto)
        else:
            connect.insertProduto(produto)
        self.produtosFrame()       

    def novoPedido(self):
        pedido = models.Pedido()
        pedido.usuario_id = self.loggedUser.pessoa_id
        pedido.cliente_id = self.loggedUser.pessoa_id
        return connect.insertPedido(pedido)
    
    def getSelectedPessoa(self):
        pos = self.listClientes.curselection()
        item = self.listClientes.get(pos)
        return int(item[3:7])

    def getSelectedProduto(self):
        pos = self.listProdutos.curselection()
        item = self.listProdutos.get(pos)
        return int(item[3:7])

    def getSelectedPedProduto(self):
        pos = self.listPedProdutos.curselection()
        produto = self.listPedProdutos.get(pos)
        return int(produto[0:4])

    def getSelectedItemProduto(self):
        pos = self.listItens.curselection()
        item = self.listItens.get(pos)
        produtoId = int(item[0:4])
        pedidoId = int(item[4:8])
        return produtoId, pedidoId

    def getSelectPedCliente(self):
        return int(self.cliente_value.get()[0:4])

    def atualizaTotalPedido(self):
        pedidoId = int(self.entryPedidoId.get())
        self.entryValorTotal.configure(state='normal')
        self.entryValorTotal.delete(0, END)
        self.entryValorTotal.insert(0, "R$: " + str(connect.selectTotalPedido(pedidoId)))
        self.entryValorTotal.configure(state='readonly')

    def onRadioStatusClienteSelect(self):
        self.carregaClientes(self.expPessoaVar.get() == "Ativos")
        self.btnDeleteCliente["text"] = "Inativar" if self.expPessoaVar.get() == "Ativos" else "Ativar"

    def onRadioStatusProdutoSelect(self):
        self.carregaProdutos(self.expProdVar.get() == "Ativos")
        self.btnDeleteProduto["text"] = "Inativar" if self.expProdVar.get() == "Ativos" else "Ativar"

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

    def carregaPedProdutos(self, onlyAtivos=True):
        produtos = connect.selectProdutos(onlyAtivos)
        self.listPedProdutos.delete(0, END)
        for item in produtos:
            self.listPedProdutos.insert(END, "%-4d Nome: %-30s  Quantidade: %-4s Preço: %-10s" %(item[0], item[1], item[3], item[4]))

    def carregaPedidos(self, onlyAtivos=True):
        pedidos = connect.selectPedidosJoin(onlyAtivos)
        self.listPedidos.delete(0, END)
        for item in pedidos:
            self.listPedidos.insert(END, "Id: %-4d Operador: %-30s Cliente: %-40s Data: %-8s Preço: %-10s" %(item[0], item[2], item[1], item[3], item[4]))

    def carregaItens(self):
        pedidoId = int(self.entryPedidoId.get())
        itens = connect.selectItens(pedidoId)
        self.listItens.delete(0, END)
        for item in itens:
            self.listItens.insert(END, "%-4d %-4d Produto: %-15s Quantidade: %-4d Preço Unit.: %-8s Preço Total: %-8s" %(item[0], item[1], item[2], item[3], item[4], item[5]))
 
    def carregaEstoque(self, onlyAtivos=True):
        produtos = connect.selectEstoqueBaixo(onlyAtivos)
        self.listEstoque.delete(0, END)
        for produto in produtos:
            self.listEstoque.insert(END, "Nome: %-18s Quantidade: %-4s" %(produto[1], produto[3]))
        
    def carregaVendas(self, onlyAtivos=True):
        pedidos = connect.selectUltimasVendas(onlyAtivos)
        self.listVendas.delete(0, END)
        for venda in pedidos:
            self.listVendas.insert(END, "Data: %-20s Cliente: %-18s Total: %-6s" %(venda[3], venda[2], venda[4]))

    def carregaBoxClientes(self):
        pessoas = connect.selectPessoas()
        clientes = []
        for pessoa in pessoas:
            clientes.append("%-4s - %-30s" %(pessoa[0], pessoa[1]))
        return clientes

    # Exibição dos dados importados

    def carregaImportados(self, imported, importedtype):
        self.listImportados.delete(0, END)
        if (importedtype == "Tudo"):
            self.importedBanco(imported)
        elif (importedtype == "Pessoas"):
            self.importedPessoas(imported)
        elif (importedtype == "Produtos"):
            self.importedProdutos(imported)
        elif (importedtype == "Pedidos"):
            self.importedPedidos(imported)
        elif (importedtype == "ItensPedidos"):
            self.importedItens(imported)

    def importedBanco(self, banco):
        self.listImportados.delete(0, END)
        self.importedPessoas(banco["Pessoas"])
        self.importedProdutos(banco["Produtos"])
        self.importedPedidos(banco["Pedidos"])
        self.importedItens(banco["ItensPedido"])
        
    def importedPessoas(self, pessoas):
        self.listImportados.insert(END, "Pessoas")
        for pessoa in pessoas:
                self.listImportados.insert(END, "Id: %-4d Nome: %-30s Email: %-25s Telefone: %-16s Endereco: %-40s" %(pessoa["pessoa_id"], pessoa["nome"], pessoa["email"], pessoa["telefone"], pessoa["endereco"])) 

    def importedProdutos(self, produtos):
        self.listImportados.insert(END, "Produtos")
        for produto in produtos:
                self.listImportados.insert(END, "Id: %-4d Nome: %-30s Quantidade: %-5s Preço: %-10s Descrição: %-30s" %(produto["produto_id"], produto["nome"], produto["quantidade"], produto["preco"], produto["descricao"])) 

    def importedPedidos(self, pedidos):
        self.listImportados.insert(END, "Pedidos")
        for pedido in pedidos:
                self.listImportados.insert(END, "Id: %-4d ClienteId: %-5s UsuarioId: %-5s Data: %-16s" %(pedido["pedido_id"], pedido["cliente_id"], pedido["usuario_id"], pedido["to_char"])) 

    def importedItens(self, itens):
        self.listImportados.insert(END, "Itens")
        for item in itens:
                self.listImportados.insert(END, "PedidoId: %-4d ProdutoId: %-5s Quantidade: %-5s Preço Unitario: %-16s" %(item["pedido_id"], item["produto_id"], item["quantidade"], item["preco"])) 

def main(user):
    app = FramePrincipal(user=user)
    app.mainloop()

#main()