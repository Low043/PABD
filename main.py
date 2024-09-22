from src.services import *
from src.models import *
from src.views import *

class NFTStore(Menu):
    def __init__(self):#Cria um Menu chamado NFTStore que possui 500px de largura e 500px de altura
        super().__init__('NFTStore','500x500')
        self.database = Builder().connect()#Se conecta ao banco de dados

        #Instancia todas as janelas do programa e adiciona elas ao Menu
        self.loginWindow = LoginWindow(self)
        self.registerWindow = RegisterWindow(self)
        self.storeWindow = StoreWindow(self)
        self.littleCarWindow = LittleCarWindow(self)

        self.addWindow(self.loginWindow)
        self.addWindow(self.registerWindow)
        self.addWindow(self.storeWindow)
        self.addWindow(self.littleCarWindow)

app = NFTStore()
app.mainloop()