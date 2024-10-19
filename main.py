import tkinter as tk
from src.views import *
from src.services.builder import *

class Desalojados(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Desalojados')
        self.geometry('400x400')
        self.database = Builder().connect()#Realiza a conexão com o banco de dados (cria caso não exista)

        #Cria uma lista de Frames (views) e posiciona-os um em cima do outro
        self.views : list[tk.Frame] = [LoginView(self), FeedView(self), EditView(self), AddView(self)]
        for view in self.views:
            view.grid(row=0,column=0,sticky='nsew')

        self.setView(self.views[0])#Coloca a tela de login acima das outras

    def setView(self,view:tk.Frame):#Coloca uma view acima das outras
        view.tkraise()

#Instanciando e iniciando o programa
desalojados = Desalojados()
desalojados.mainloop()