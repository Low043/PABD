import tkinter as tk
from tkinter import messagebox
from src.services.sqlManager import *
from src.models import *

class LoginView(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(list(range(11)), weight=1)

        userLabel = tk.Label(self, text='Usuário')
        userLabel.grid(row=3, column=0, padx=50, sticky='w')

        self.userEntry = tk.Entry(self)
        self.userEntry.grid(row=4, column=0, padx=50, ipady=5, sticky='ew')

        passwordLabel = tk.Label(self, text='Senha')
        passwordLabel.grid(row=5, column=0, padx=50, sticky='w')

        self.passwordEntry = tk.Entry(self)
        self.passwordEntry.grid(row=6, column=0, padx=50, ipady=5, sticky='ew')

        loginButton = tk.Button(self, text='Login', command=self.login)
        loginButton.grid(row=7, column=0, padx=50, pady=20, ipady=5, sticky='ew')

    def login(self):
        user = self.userEntry.get()
        password = self.passwordEntry.get()

        if user == '' or password == '':
            return messagebox.showerror('Erro de Login', 'Usuário ou senha em branco')
        
        try:#Tenta acessar o primeiro usuário que corresponda ao usuário e senha digitados
            result = self.master.database.getFrom('Users',where=[('userName',user),('userPassword',password)])[0]
            self.master.user = User(result)
            self.master.setView(self.master.views[1])
        except:#Caso esse usuário não exista, ocorre um erro por tentar acessar um valor inválido em uma lista
            messagebox.showerror('Erro de Login', 'Usuário ou senha incorretos')