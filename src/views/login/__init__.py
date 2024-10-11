from src.services.sqlManager import *
from src.models.user import *
from termcolor import colored

class LoginView:
    def __init__(self,app):
        self.app = app

    def authenticate(self,user:str,password:str):
        try:#Try get User
            result = self.app.database.getFrom(tableName='Users',where=[('userName',user),('userPass',password)])[0]

            self.app.user = User(ID=result[0],name=result[1],password=result[2])

            print(colored(f'Usuário {result[1]} ({result[0]}) acessado com sucesso','blue'))
            
            return result
        except:#Cannot find
            print(colored(f'Usuário não encontrado','magenta'))
            return None