from src.services import *
from src.models import *
from src.views import *

class NFTStore(Menu):
    def __init__(self):
        super().__init__('NFTStore','500x500')
        self.database = Builder().connect()

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