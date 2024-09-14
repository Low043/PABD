from src.services import *

class LoginWindow(Window):
    def __init__(self,app):
        super().__init__(app,'Login')

        title = Container(self,text='NFTStore',font=('Arial',32))
        self.addElement(title,3,2,3)

        user = Input(self,'Usuário',height=48)
        self.addElement(user,2,4,5,expandTo='ew')

        password = Input(self,'Senha',password=True,height=48)
        self.addElement(password,2,5,5,expandTo='ew')

        login = Button(self,'Entrar',height=48,color='#0e822d',hoverColor='#0b6323')
        self.addElement(login,2,6,5,expandTo='ew')

        register = Button(self,'Criar usuário',color='transparent',hover=False)
        self.addElement(register,3,7,3,expandTo='')