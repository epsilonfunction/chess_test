
class piece():
    def __init__(self,name,alive,colour,position):
        self.name = name
        self.alive = alive
        self.colour = colour
        self.position = position
    #def check():
        #if

class Black(piece):
    def __init__(self):
        super().__init__(name,alive,colour,position)
        self.colour = "Black"
        

class Queen(piece):
    def __init__(self):
        super().__init__(alive,colour,position)
        self.type = "Queen"
    def available_moves():
        list = []
            

x = Black()
print(x.name)
