class House:
    def __init__(self,house:tuple):
        self.id : int = house[0]
        self.owner : int = house[1]
        self.address : str = house[2]
        self.available : bool = house[3]