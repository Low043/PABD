class User:
    def __init__(self,user:tuple):
        self.id : int = user[0]
        self.name : str = user[1]
        self.password : str = user[2]