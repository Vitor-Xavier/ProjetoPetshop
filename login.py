from tkinter import *
from tkinter import messagebox as mbox
import PetShop

class FramePrincipal(Frame):

    def __init__(self, master=None):
        super().__init__()
        self.master.geometry("300x190")
        self.master.title("Pet Shop")
        #self.master.iconbitmap("res/icon.ico")
        self.master.configure(background="white")
        self.master.resizable(False, False)
        self.pack()

        # Frame titulo
        self.frameTitle = Frame(bg=PetShop.FramePrincipal._barColor, height=60)
        self.frameTitle.pack(fill=X)

        self.lblTitle = Label(self.frameTitle)
        self.lblTitle["text"] = "Login"
        self.lblTitle["bg"] = PetShop.FramePrincipal._barColor
        self.lblTitle["fg"] = PetShop.FramePrincipal._primaryTextColor
        self.lblTitle["font"] = PetShop.FramePrincipal._fontSubtitle
        self.lblTitle.pack(side=TOP, ipady=15)

        # Frame Usuário
        self.frameUser = Frame(bg=PetShop.FramePrincipal._backgroundColor, height=40)
        self.frameUser.pack(fill=X)

        self.lblUsuario = Label(self.frameUser)
        self.lblUsuario["text"] = "Usuário"
        self.lblUsuario["bg"] = PetShop.FramePrincipal._backgroundColor
        self.lblUsuario.pack(side=LEFT, ipady=10, ipadx=10)

        self.entryUsuario = Entry(self.frameUser, width=22)
        self.entryUsuario["bg"] = PetShop.FramePrincipal._backgroundColor
        self.entryUsuario.bind("<Return>", self.trocarFoco)
        self.entryUsuario.pack(side=LEFT)
        self.entryUsuario.focus_set()

        # Frame Senha
        self.frame3 = Frame(bg=PetShop.FramePrincipal._backgroundColor, height=40)
        self.frame3.pack(fill=X)

        self.lblSenha = Label(self.frame3)
        self.lblSenha["text"] = "Senha: "
        self.lblSenha["bg"] = PetShop.FramePrincipal._backgroundColor
        self.lblSenha.pack(side=LEFT, ipady=10, ipadx=10)

        self.entrySenha = Entry(self.frame3, width=22)
        self.entrySenha["bg"] = PetShop.FramePrincipal._backgroundColor
        self.entrySenha["show"] = "*"
        self.entrySenha.pack(side=LEFT)

        # Frame Botões
        self.frame4 = Frame(bg=PetShop.FramePrincipal._backgroundColor, height=40)
        self.frame4.pack(fill=X)

        self.btnLogin = Button(self.frame4, width=10)
        self.btnLogin["text"] = "Entrar"
        self.btnLogin["bg"] = PetShop.FramePrincipal._backgroundColor
        self.btnLogin["command"] = self.btnLoginClick 
        self.btnLogin.pack(side=RIGHT, padx=15, pady=1)

        self.btnClear = Button(self.frame4, width=10)
        self.btnClear["text"] = "Limpar"
        self.btnClear["bg"] = PetShop.FramePrincipal._backgroundColor
        self.btnClear["command"] = self.btnClearClick 
        self.btnClear.pack(side=RIGHT, pady=1)

    # Tratadores de eventos
    def trocarFoco(self, event):
        self.entrySenha.focus_set()

    def btnLoginClick(self):
        self.frameTitle.destroy()
        self.frameUser.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        PetShop.main()

    def btnClearClick(self):
        self.entrySenha[""]

    def exibirMensagem(self, msg):
        mbox.showinfo("Pet Shop", msg) 

app = FramePrincipal()
app.mainloop()