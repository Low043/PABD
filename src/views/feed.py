import tkinter as tk
from tkinter import messagebox
from src.models import *

class FeedView(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        backButton = tk.Button(self, text='Voltar', command=self.backToLogin)
        backButton.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        editButton = tk.Button(self, text='Editar', command=self.goToEditView)
        editButton.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        addButton = tk.Button(self, text='Adicionar', command=self.goToAddView)
        addButton.grid(row=0, column=2, sticky='e', padx=5, pady=5)

        feedFrame = tk.Frame(self)
        feedFrame.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
        scrollbar = tk.Scrollbar(feedFrame, orient='vertical')

        self.houseList = tk.Listbox(feedFrame, yscrollcommand=scrollbar.set, height=15)
        self.houseList.pack(side='left', fill='both', expand=True)

        scrollbar.config(command=self.houseList.yview)
        scrollbar.pack(side='right', fill='y')

        rentTimeLabel = tk.Label(self, text='Dias de aluguel:')
        rentTimeLabel.grid(row=2, column=0, pady=10)

        self.rentTimeEntry = tk.Entry(self)
        self.rentTimeEntry.grid(row=2, column=1, pady=10)

        rentButton = tk.Button(self, text='Alugar', command=self.rent)
        rentButton.grid(row=2, column=2, pady=10)

    def backToLogin(self):
        self.master.setView(self.master.views[0])

    def goToEditView(self):
        self.master.setView(self.master.views[2])

    def goToAddView(self):
        self.master.setView(self.master.views[3])

    def rent(self):
        houseSelected = self.houseList.curselection()
        if houseSelected:
            houseSelected = self.houseList.get(houseSelected)
            rentTime = self.rentTimeEntry.get()
            if rentTime:
                print(f'Alugando o imóvel: {houseSelected} por {rentTime} dias')
            else:
                messagebox.showerror("Erro de Aluguel", "Defina um período de aluguel")
        else:
            messagebox.showerror("Erro de Aluguel", "Selecione uma casa para alugar")

    def constructor(self):
        self.houseList.delete(0, tk.END)
        houseList = self.master.database.getFrom('Houses',where=[('available',True)])
        for value in houseList:
            house = House(value)
            self.houseList.insert(tk.END, house.address)