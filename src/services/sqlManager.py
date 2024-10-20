from termcolor import colored
import psycopg2

'''
    O método join() vai ser muito usado nesse arquivo, o que ele faz é transformar uma lista de elementos em uma string.
    Ex: ','.join([1,2,3]) = '1,2,3';
    Ex: ' AND '.join([1,2,3]) = '1 AND 2 AND 3'
'''

class SqlVar:#Ajuda a referenciar tipos de dados SQL (int, varchar, bool). Variações dessa classe no final do arquivo
    def __init__(self,name:str,notNull:bool=False):
        self.name = name
        self.notNull = notNull

    def null(self):
        return 'not null' if self.notNull else ''

class Database:
    def __init__(self,name:str,userName:str,hostName:str,password:str,port:int):#Estabelece uma conexão autocomitada com um banco de dados
        self.connection = psycopg2.connect(database=name,user=userName,host=hostName,password=password,port=port)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def execute(self,sqlCommand:str):#Executa um comando sql e retorna/exibe se ele foi bem sucedido
        try:
            self.cursor.execute(sqlCommand)
            print(colored(sqlCommand,'light_green'))
            return True
        except Exception as e:
            print(colored(e,'red'))
            return False
    
    def columnValue(self,values:list[tuple]) -> list[str]:#Transforma uma lista de tuplas [(coluna,valor)] em uma lista de strings ["coluna = valor"]
        #Esse método também adiciona aspas caso o valor seja uma string e corrige o nome da coluna para minúsculo
        newValues = []
        for value in values:
            if type(value[1]) == str:
                newValues.append(f"{value[0].lower()} = '{value[1]}'")
            else:
                newValues.append(f'{value[0].lower()} = {value[1]}')
        return newValues

    def createTable(self,tableName:str,columns:list[SqlVar]):#Cria uma tabela
        columns = ','.join(str(column) for column in columns)
        sqlCommand = f'CREATE TABLE {tableName} ({columns})'

        return self.execute(sqlCommand)

    def insertIn(self,tableName:str,columns:list[str],values:list):#Insere valores em colunas de uma tabela
        columns = ','.join(columns)
        
        newValues = []
        for value in values:
            if type(value) == str:#Adiciona aspas caso os valores a serem inseridos sejam strings
                newValues.append(f"'{value}'")
            else:
                newValues.append(str(value))

        sqlCommand = f'INSERT INTO {tableName} ({columns}) VALUES ({','.join(newValues)})'

        return self.execute(sqlCommand)
    
    def update(self,tableName:str,setValues:list[tuple],where:list[tuple]):#Atualiza valores já existentes em uma tabela
        setValues = self.columnValue(setValues)
        where = self.columnValue(where)
        
        sqlCommand = f'UPDATE {tableName} SET {','.join(setValues)} WHERE {' AND '.join(where)}'
        
        return self.execute(sqlCommand)
    
    def deleteFrom(self,tableName:str,where:list[tuple]):#Apaga elementos de uma tabela
        where = self.columnValue(where)

        sqlCommand = f'DELETE FROM {tableName} WHERE {' AND '.join(where)}'

        return self.execute(sqlCommand)
    
    def getFrom(self,tableName:str,columns:list[str]='*',where:list[tuple]=[]):#Retorna uma tupla de ocorrências em uma tabela
        if type(columns) == list:
            columns = f'({",".join(columns)})'

        where = self.columnValue(where)

        sqlCommand = f'SELECT {columns} FROM {tableName.lower()} {f"WHERE {' AND '.join(where)}" if where else ""}'

        if self.execute(sqlCommand):
            return self.cursor.fetchall()
        return False

    def close(self):#Encerra a conexão com o banco de dados
        self.cursor.close()
        self.connection.close()

#Tipos de dados SQL e suas representações em String para facilitar o createTable()
class Pk(SqlVar):
    def __init__(self,name:str,type:str='SERIAL'):
        super().__init__(name)
        self.type = type

    def __str__(self):
        return f'{self.name} {self.type} PRIMARY KEY'

class Fk(SqlVar):
    def __init__(self,name:str,referenceTable:str,referenceVar:str):
        super().__init__(name)
        self.referenceTable = referenceTable
        self.referenceVar = referenceVar

    def __str__(self):
        return f'{self.name} int REFERENCES {self.referenceTable} ({self.referenceVar}) ON DELETE CASCADE'
    
class Varchar(SqlVar):
    def __init__(self,name:str,size:int,notNull:bool=True):
        super().__init__(name,notNull)
        self.size = size
    
    def __str__(self):
        return f'{self.name} varchar({self.size}) {self.null()}'

class Int(SqlVar):
    def __init__(self,name:str,notNull:bool=True):
        super().__init__(name,notNull)

    def __str__(self):
        return f'{self.name} int {self.null()}'
    
class Float(SqlVar):
    def __init__(self,name:str,notNull:bool=True):
        super().__init__(name,notNull)

    def __str__(self):
        return f'{self.name} float {self.null()}'
    
class Bool(SqlVar):
    def __init__(self,name:str,notNull:bool=True):
        super().__init__(name,notNull)

    def __str__(self):
        return f'{self.name} boolean {self.null()}'