import tkinter as tk
from tkinter import messagebox

class AddView(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        backButton = tk.Button(self, text='Voltar', command=self.backToFeed)
        backButton.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        addressLabel = tk.Label(self, text='Endereço:')
        addressLabel.grid(row=1, column=0, padx=50, pady=(120,0), sticky='w')

        #Adiciona uma 'validação de entrada' que impede entradas maiores que 50 dígitos
        self.addressEntry = tk.Entry(self, validate='key', validatecommand=(self.register(self.validateAddress), '%P'))
        self.addressEntry.grid(row=2, column=0, padx=50, pady=10, sticky='ewn')

        addButton = tk.Button(self, text='Adicionar', command=self.addHouse)
        addButton.grid(row=3, column=0, padx=50, pady=20, ipady=5, sticky='ew')

    def validateAddress(self, input:str):#Regra de validação de endereço
        if len(input) <= 50:
            return True
        else:
            return False

    def backToFeed(self):
        self.master.setView(self.master.views[1])

    def addHouse(self):#Adiciona uma nova casa a lista de casas disponíveis
        address = self.addressEntry.get()

        result = self.master.database.getFrom('Houses',where=[('address',address)])
        if result != []:
            return messagebox.showerror('Erro', 'Este endereço já está registrado')

        if address == '':
            return messagebox.showerror('Erro', 'O campo de endereço está vazio!')

        self.master.database.insertIn('Houses', ['owner','address', 'available'], values=[self.master.user.id,address,True])

        #Limpa o endereço
        self.addressEntry.delete(0, tk.END)

        messagebox.showinfo('Sucesso', 'Casa adicionada com sucesso!')