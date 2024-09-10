from src.services.sqlManager import *

class Builder:
    def __init__(self):
        self.databaseName = 'nftstore'
        self.userName = 'postgres'
        self.host = 'localhost'
        self.password = 'pabd'
        self.port = 5432

    def connect(self):
        try:#Tenta acessar o banco de dados
            return Database(self.databaseName,self.userName,self.host,self.password,self.port)
        except:#Caso haja algum erro (banco de dados não existe) cria o banco de dados
            return self.createDatabase()
        
    def createDatabase(self):#Acessa o banco de dados padrão (postgres) e cria o banco de dados nftstore
        database = Database('postgres',self.userName,self.host,self.password,self.port)
        database.execute(f'CREATE DATABASE {self.databaseName}')
        database.close()
        return Database(self.databaseName,self.userName,self.host,self.password,self.port)