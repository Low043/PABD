from src.services.sqlManager import *

class Builder:
    def __init__(self):#Configurações do banco de dados (altere caso necessário)
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
        
    def createDatabase(self):#Acessa o banco de dados padrão (postgres) e constrói o banco de dados desalojados
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
            Varchar('address',size=50),
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
        
        database.insertIn('Houses',['address','available'],['Rua Trabalho de Última Hora, nº70',True])
        database.insertIn('Houses',['address','available'],['Rua Daniel Me Dá Nota Máxima, nº38',True])
        database.insertIn('Houses',['address','available'],['Rua João Félix de Nascimento, nº129',True])

        return database