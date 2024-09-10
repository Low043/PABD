import psycopg2

class Database:
    def __init__(self,name:str,userName:str,hostName:str,password:str,port:int):
        self.connection = psycopg2.connect(database=name,user=userName,host=hostName,password=password,port=port)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def execute(self,sqlCommand:str):
        try:
            self.cursor.execute(sqlCommand)
            return True
        except:
            return False

    def createTable(self,tableName:str,columns:list[str]):
        columns = ','.join(columns)#Comma separated columns
        sqlCommand = f'CREATE TABLE {tableName} ({columns})'

        return self.execute(sqlCommand)
        
    def insertIn(self,tableName:str,columns:list[str],values:list[str]):
        columns = ','.join(columns)#Comma separated columns and values
        values = ','.join(values)
        sqlCommand = f'INSERT INTO {tableName} ({columns}) VALUES ({values})'

        return self.execute(sqlCommand)
    
    def update(self,columnName:str,inTable:str,where:str,setValue):
        if type(value) == str:
            value = f'"{value}"'
        sqlCommand = f'UPDATE {inTable} SET {columnName}={setValue} WHERE {where}'

        return self.execute(sqlCommand)
    
    def delete(self,tableName:str,where:str):
        sqlCommand = f'DELETE FROM {tableName} WHERE {where}'

        return self.execute(sqlCommand)
    
    def getFrom(self,table:str,columns:list='*',where:str=''):
        if type(columns) == list:
            columns = f'({",".join(columns)})'
        sqlCommand = f'SELECT {columns} FROM {table} {f"WHERE {where}" if where else ""}'

        if self.execute(sqlCommand):
            return self.cursor.fetchall()
        return False

    def close(self):
        self.cursor.close()
        self.connection.close()
