from src.services import *

class LoginWindow(Window):
    def __init__(self,app):
        super().__init__(app,'Login')

        title = Container(self,text='NFTStore',font=('Arial',48))
        self.addElement(title,3,2,3,expandTo='')

        user = Input(self,'Usuário',height=48)
        self.addElement(user,3,4,3,expandTo='ew')

        password = Input(self,'Senha',password=True,height=48)
        self.addElement(password,3,5,3,expandTo='ew')

        showPass = ViewPassButton(self,password,images=(Image('src/images/show-password.png',size=(32,32)),Image('src/images/hide-password.png',size=(32,32))))
        self.addElement(showPass,6,5)

        login = Button(self,'Entrar',height=48,color='#0e822d',hoverColor='#0b6323')
        self.addElement(login,3,6,3,expandTo='ew')

        register = Button(self,'Criar usuário',color='transparent',hover=False)
        self.addElement(register,3,7,3,expandTo='')