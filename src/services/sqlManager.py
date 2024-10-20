from termcolor import colored
import psycopg2

class SqlVar:#Base para a representação dos tipos de dados SQL
    def __init__(self,name:str,notNull:bool=False):
        self.name = name
        self.notNull = notNull

    def null(self):
        return 'not null' if self.notNull else ''

class Database:
    def __init__(self,name:str,userName:str,hostName:str,password:str,port:int):
        self.connection = psycopg2.connect(database=name,user=userName,host=hostName,password=password,port=port)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def execute(self,sqlCommand:str):#Executa um comando sql e retorna se ele foi bem sucedido ou não
        try:
            self.cursor.execute(sqlCommand)
            print(colored(sqlCommand,'light_green'))
            return True
        except Exception as e:
            print(colored(e,'red'))
            return False

    def createTable(self,tableName:str,columns:list[SqlVar]):
        columns = ','.join(str(column) for column in columns)#Transforma a lista de SqlVar em uma string separada por vírgula
        sqlCommand = f'CREATE TABLE {tableName} ({columns})'

        return self.execute(sqlCommand)

    def insertIn(self,tableName:str,columns:list[str],values:list):
        columns = ','.join(columns)#Transforma as listas de SqlVar em strings separadas por vírgula
        
        newValues = []
        for value in values:
            if type(value) == str:
                newValues.append(f"'{value}'")
            else:
                newValues.append(str(value))

        values = ','.join(newValues)
        sqlCommand = f'INSERT INTO {tableName} ({columns}) VALUES ({values})'

        return self.execute(sqlCommand)
    
    def update(self,columnName:str,inTable:str,where:list[tuple],setValue):#Atualiza valores já existentes em uma tabela
        if type(setValue) == str:
            setValue = f'"{setValue}"'
        
        newWhere = []
        for item in where:
            if type(item[1]) == str:
                newWhere.append(f"{item[0].lower()} = '{item[1]}'")
            else:
                newWhere.append(f'{item[0].lower()} = {item[1]}')
            
        sqlCommand = f'UPDATE {inTable} SET {columnName}={setValue} WHERE {' AND '.join(newWhere)}'

        return self.execute(sqlCommand)
    
    def deleteIn(self,tableName:str,where:str):
        sqlCommand = f'DELETE FROM {tableName} WHERE {where}'

        return self.execute(sqlCommand)
    
    def getFrom(self,tableName:str,columns:list[str]='*',where:list[tuple]=[]):#Retorna uma tupla de ocorrências em uma tabela
        if type(columns) == list:
            columns = f'({",".join(columns)})'

        newWhere = []#Coloca aspas em valores que são strings
        for item in where:
            if type(item[1]) == str:
                newWhere.append(f"{item[0].lower()} = '{item[1]}'")
            else:
                newWhere.append(f'{item[0].lower()} = {item[1]}')

        sqlCommand = f'SELECT {columns} FROM {tableName.lower()} {f"WHERE {' AND '.join(newWhere)}" if newWhere else ""}'

        if self.execute(sqlCommand):
            return self.cursor.fetchall()
        return False

    def close(self):
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