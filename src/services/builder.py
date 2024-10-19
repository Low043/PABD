from src.services.sqlManager import *

class Builder:
    def __init__(self):
        self.databaseName = 'desalojados'
        self.userName = 'postgres'
        self.host = 'localhost'
        self.password = 'pabd'
        self.port = 5432

    def connect(self) -> Database:
        try:#Tenta acessar o banco de dados
            return Database(self.databaseName,self.userName,self.host,self.password,self.port)
        except:#Caso haja algum erro (banco de dados não existe) cria o banco de dados
            return self.createDatabase()
        
    def createDatabase(self):#Acessa o banco de dados padrão (postgres) e cria o banco de dados desalojados
        database = Database('postgres',self.userName,self.host,self.password,self.port)
        database.execute(f'CREATE DATABASE {self.databaseName}')
        database.close()

        database = Database(self.databaseName,self.userName,self.host,self.password,self.port)

        database.createTable('Users',columns=[
            Pk('userID'),
            Varchar('userName',size=20),
            Varchar('userPassword',size=20)
        ])

        database.createTable('Houses',columns=[
            Pk('houseID'),
            Varchar('address',size=20),
            Bool('available')
        ])

        database.createTable('Rentings',columns=[
            Pk('RentingID'),
            Fk('userID',referenceTable='Users',referenceVar='userID'),
            Fk('houseID',referenceTable='Houses',referenceVar='houseID'),
            Int('rentingTime')
        ])

        database.insertIn('Users',['userName','userPassword'],values=['Daniel','pabd'])
        database.insertIn('Users',['userName','userPassword'],values=['Luis','desalojado'])

        return database