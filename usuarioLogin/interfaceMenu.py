import customtkinter as ctk
from sqlManager import *

class LoginMenu(ctk.CTk):
    def __init__(self,database:Database):
        super().__init__()
        self.title('Luís Gustavo')
        self.geometry('400x400')
        self.resizable(False,False)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(list(range(51)),weight=1)
        self.database = database

        elementWidth = 200

        loginText = ctk.CTkLabel(self,text='Fazer Login',font=('Arial',24),width=elementWidth)
        loginText.grid(column=1,row=19,pady=0)

        self.userNameInput = ctk.CTkEntry(self,placeholder_text='Usuário',width=elementWidth,justify='center')
        self.userNameInput.grid(column=1,row=23,pady=0)

        self.passwordInput = ctk.CTkEntry(self,placeholder_text='Senha',width=elementWidth,justify='center')
        self.passwordInput.grid(column=1,row=24,pady=0)

        loginButton = ctk.CTkButton(self,text='Entrar',width=elementWidth,command=self.login)
        loginButton.grid(column=1,row=25,pady=0)

        signInText = ctk.CTkLabel(self,text='Criar uma conta',font=('Arial',12),width=elementWidth)
        signInText.grid(column=1,row=26,pady=0)

    def login(self):
        correctPassword = self.database.getFrom('UserLogin','userPassword',where=f"userName='{self.userNameInput.get()}'")
        if correctPassword != [] and self.passwordInput.get() == correctPassword[0][0]:
            print('Login efetuado com sucesso!')
            return True
        print('Usuário ou senha incorretos')