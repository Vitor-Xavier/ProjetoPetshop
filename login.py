from tkinter import *
from tkinter import messagebox as mbox
import PetShop
import connect

class FramePrincipal(Frame):

    def __init__(self, master=None):
        super().__init__()
        self.centralizar(300, 190)
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
        self.frameSenha = Frame(bg=PetShop.FramePrincipal._backgroundColor, height=40)
        self.frameSenha.pack(fill=X)

        self.lblSenha = Label(self.frameSenha)
        self.lblSenha["text"] = "Senha: "
        self.lblSenha["bg"] = PetShop.FramePrincipal._backgroundColor
        self.lblSenha.pack(side=LEFT, ipady=10, ipadx=10)

        self.entrySenha = Entry(self.frameSenha, width=22)
        self.entrySenha["bg"] = PetShop.FramePrincipal._backgroundColor
        self.entrySenha["show"] = "*"
        self.entrySenha.pack(side=LEFT)

        # Frame Botões
        self.frameButtons = Frame(bg=PetShop.FramePrincipal._backgroundColor, height=40)
        self.frameButtons.pack(fill=X)

        self.btnLogin = Button(self.frameButtons, width=10)
        self.btnLogin["text"] = "Entrar"
        self.btnLogin["bg"] = PetShop.FramePrincipal._backgroundColor
        self.btnLogin["command"] = self.btnLoginClick 
        self.btnLogin.pack(side=RIGHT, padx=15, pady=1)

        self.btnClear = Button(self.frameButtons, width=10)
        self.btnClear["text"] = "Limpar"
        self.btnClear["bg"] = PetShop.FramePrincipal._backgroundColor
        self.btnClear["command"] = self.btnClearClick 
        self.btnClear.pack(side=RIGHT, pady=1)

    def centralizar(self, largura, altura):
        px = int((self.master.winfo_screenwidth() - largura) / 2)
        py = int((self.master.winfo_screenheight() - altura) / 2)
        self.master.geometry("{}x{}+{}+{}".format(largura, altura, px, py))

    # Tratadores de eventos
    def trocarFoco(self, event):
        self.entrySenha.focus_set()

    def btnLoginClick(self):
        if (len(self.entryUsuario.get()) == 0):
            self.exibirMensagem("Preencha o campo email")
            return
        if (len(self.entrySenha.get()) == 0):
            self.exibirMensagem("Preencha o campo senha")
            return
        email = self.entryUsuario.get()
        senha = self.entrySenha.get()
        connect.login(email, senha)
        if (connect.login(email, senha)):
            self.destroyFrame()
            PetShop.main()
        else:
            self.exibirMensagem("Login incorreto.")

    def destroyFrame(self):
        self.frameTitle.destroy()
        self.frameUser.destroy()
        self.frameSenha.destroy()
        self.frameButtons.destroy()

    def btnClearClick(self):
        self.entryUsuario.delete(0, 'end')
        self.entrySenha.delete(0, 'end')

    def exibirMensagem(self, msg):
        mbox.showinfo("Pet Shop", msg) 

app = FramePrincipal()
app.mainloop()