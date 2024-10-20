import tkinter as tk
from tkinter import messagebox
from src.models import *

class EditView(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(list(range(2)), weight=1)

        backButton = tk.Button(self, text='Voltar', command=self.backToFeed)
        backButton.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        rentedLabel = tk.Label(self, text='Casas Alugadas:')
        rentedLabel.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        rentedFrame = tk.Frame(self)
        rentedFrame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew', columnspan=2)

        rentedScrollbar = tk.Scrollbar(rentedFrame, orient='vertical')
        self.rentedList = tk.Listbox(rentedFrame, yscrollcommand=rentedScrollbar.set, height=5)
        self.rentedList.pack(side='left', fill='both', expand=True)
        rentedScrollbar.config(command=self.rentedList.yview)
        rentedScrollbar.pack(side='right', fill='y')

        rentTimeLabel = tk.Label(self, text='Novo tempo de aluguel:')
        rentTimeLabel.grid(row=3, column=0, padx=5, pady=5, sticky='w')

        self.rentTimeEntry = tk.Entry(self, validate='key', validatecommand=(self.register(self.validateRentTime), '%P'))
        self.rentTimeEntry.grid(row=4, column=0, padx=5, pady=5, sticky='ew', columnspan=2)

        editRentButton = tk.Button(self, text='Editar Aluguel', command=self.editRent)
        editRentButton.grid(row=5, column=0, padx=5, pady=5, sticky='ew')

        cancelRentButton = tk.Button(self, text='Cancelar Aluguel', command=self.cancelRent)
        cancelRentButton.grid(row=5, column=1, padx=5, pady=5, sticky='ew')

        ownedLabel = tk.Label(self, text='Casas Disponíveis para Alugar:')
        ownedLabel.grid(row=6, column=0, padx=5, pady=5, sticky='w')

        ownedFrame = tk.Frame(self)
        ownedFrame.grid(row=7, column=0, padx=5, pady=5, sticky='nsew', columnspan=2)

        ownedScrollbar = tk.Scrollbar(ownedFrame, orient='vertical')
        self.ownedList = tk.Listbox(ownedFrame, yscrollcommand=ownedScrollbar.set, height=5)
        self.ownedList.pack(side='left', fill='both', expand=True)
        ownedScrollbar.config(command=self.ownedList.yview)
        ownedScrollbar.pack(side='right', fill='y')

        removeOwnedButton = tk.Button(self, text='Remover Casa', command=self.removeOwnedHouse)
        removeOwnedButton.grid(row=8, column=0, padx=5, pady=5, sticky='ew', columnspan=2)

    def validateRentTime(self, input:str):#Regra de validação do tempo de aluguel
        if input.isdigit() and len(input) <= 3 or input == '':
            return True
        else:
            return False

    def backToFeed(self):
        self.master.setView(self.master.views[1])

    def constructor(self):#Busca por todos as casas alugadas e colocadas para alugar pelo usuário
        self.rentedList.delete(0, tk.END)
        self.ownedList.delete(0, tk.END)

        userRentings = self.master.database.getFrom('Rentings', where=[('userID', self.master.user.id)])
        userHouses = self.master.database.getFrom('Houses', where=[('owner', self.master.user.id)])

        for renting in userRentings:
            renting = Renting(renting)
            rentedHouse = House(self.master.database.getFrom('Houses',where=[('houseID',renting.houseId)])[0])
            self.rentedList.insert(tk.END, f'{rentedHouse.address} (Alugado por {renting.time} dias)')

        for house in userHouses:
            house = House(house)
            self.ownedList.insert(tk.END, house.address)

    def editRent(self):
        selected = self.rentedList.curselection()
        rentTime = self.rentTimeEntry.get()

        if not selected:
            return messagebox.showerror('Erro', 'Selecione uma casa para editar o tempo de aluguel')

        if rentTime == '':
            return messagebox.showerror('Erro', 'Defina um período de aluguel')

        #Atualiza o tempo de aluguel no banco de dados
        houseAddress = self.rentedList.get(selected).split(' (')[0]
        house = self.master.database.getFrom('Houses', where=[('address', houseAddress)])[0]

        self.master.database.update('Rentings', setValues=[('rentingTime', int(rentTime))], where=[('houseID', house[0])])

        #Atualiza o item específico da lista com o novo tempo de aluguel
        updatedText = f'{houseAddress} (Alugado por {rentTime} dias)'
        self.rentedList.delete(selected)#Remove o item anterior
        self.rentedList.insert(selected, updatedText)#Insere o novo item no mesmo lugar

        self.rentTimeEntry.delete(0, tk.END)#Limpa a entrada de dias
        messagebox.showinfo('Sucesso', 'Tempo de aluguel atualizado com sucesso')

    def cancelRent(self):#Cancela um aluguel (volta o status de available)
        selected = self.rentedList.curselection()

        if not selected:
            return messagebox.showerror('Erro', 'Selecione uma casa para cancelar o aluguel')

        houseAddress = self.rentedList.get(selected).split(' (')[0]
        house = House(self.master.database.getFrom('Houses', where=[('address', houseAddress)])[0])

        self.master.database.update('Houses', setValues=[('available', True)], where=[('houseID', house.id)])
        self.master.database.deleteFrom('Rentings',where=[('userID',self.master.user.id),('houseID',house.id)])

        self.rentedList.delete(selected)#Apaga da lista

        messagebox.showinfo('Sucesso', 'Aluguel cancelado com sucesso')

    def removeOwnedHouse(self):
        selected = self.ownedList.curselection()

        if not selected:
            return messagebox.showerror('Erro', 'Selecione uma casa para remover')

        houseAddress = self.ownedList.get(selected)
        house = self.master.database.getFrom('Houses', where=[('address', houseAddress)])[0]

        #Remove a casa do banco de dados
        self.master.database.deleteFrom('Houses', where=[('houseID', house[0])])

        #Remove o item da Listbox diretamente
        self.ownedList.delete(selected)

        messagebox.showinfo('Sucesso', 'Casa removida com sucesso')