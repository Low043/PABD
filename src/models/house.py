class House:
    def __init__(self,house:tuple):
        self.id : int = house[0]
        self.address : str = house[1]
        self.available : bool = house[2]