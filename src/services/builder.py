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

        database = Database(self.databaseName,self.userName,self.host,self.password,self.port)

        database.createTable('Users',columns=[
            Pk('userID'),
            Varchar('userName',size=20),
            Varchar('userPass',size=20)
        ])

        database.createTable('Nfts',columns=[
            Pk('nftID'),
            Varchar('nftName',size=20),
            Float('nftPrice')
        ])

        database.createTable('Purchases',columns=[
            Pk('purchaseID'),
            Fk('userID',referenceTable='Users',referenceVar='userID'),
            Fk('nftID',referenceTable='Nfts',referenceVar='nftID'),
            Int('amount'),
            Bool('effected')
        ])