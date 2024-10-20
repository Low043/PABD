import tkinter as tk
from src.views import *
from src.services.builder import *

class Desalojados(tk.Tk):#Janela principal e configurações iniciais do programa
    def __init__(self,user=None,startAtView=0):
        #Configurações da janela
        super().__init__()
        self.title('Desalojados')
        self.geometry('400x400')
        self.resizable(False,False)

        #Configurações de layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Realiza a conexão com o banco de dados (cria caso não exista)
        self.database = Builder().connect()
        self.user = user

        #Cria uma lista de Frames (views) e posiciona-os um em cima do outro
        self.views : list[tk.Frame] = [LoginView(self), FeedView(self), EditView(self), AddView(self)]
        for view in self.views:
            view.grid(row=0,column=0,sticky='nsew')

        self.setView(self.views[startAtView])

    def setView(self,view:tk.Frame):#Coloca uma view acima das outras
        view.tkraise()
        #Caso a janela possua um método "constructor" para ser iniciada corretamente, chama-o
        if callable(getattr(view, 'constructor', None)):
            view.constructor()

#Instanciando e iniciando o programa
desalojados = Desalojados(user=User((2,'Luis','desalojado')),startAtView=3)
desalojados.mainloop()