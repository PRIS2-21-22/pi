class Punto():
    #Constructor de la clase Punto
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def set_coord(self,cordX, cordY):
        self.x = cordX
        self.y = cordY

    def toString(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


