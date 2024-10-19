class Renting:
    def __init__(self,renting:tuple):
        self.id : int = renting[0]
        self.userId : int = renting[1]
        self.houseId : int = renting[2]
        self.time : int = renting[3]