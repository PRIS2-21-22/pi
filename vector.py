import math
import punto

class Vector:

    def __init__(self, punto1 ,punto2):
        self.punto1= punto1
        self.punto2 = punto2

    
    def CoordenadaX(self):
        return self.punto2.get_x() - self.punto1.get_x()

    def CoordenadaY(self):
        return self.punto2.get_y() - self.punto1.get_y()

    def ModuloVector(self):
        return math.sqrt(math.pow(self.cX(),2) + math.pow(self.cY(),2))

    def ProductovectorialVector(self,vector):
        return self.cX()*vector.cY()- self.cY*vector.cX()

    def EcuacionDeLaRecta(self):
        #ecuacion: y=[(y2-y1)/(x2-x1)]*(x-x1)+y1
        return f"y = {((self.punto2.get_y()-self.punto1.get_y())/(self.punto2.get_x()-self.punto1.get_x()))}*(x-{self.punto1.get_x()}) + {self.punto1.get_y()}"

    def EcuacionDeLaRecta2(self, m, b):
        #ecuacion: y = mx+b
        return f"y = {m}*x + {b}"
    
    def EcuacionDeLaRecta3(self, m, punto):
        #ecuacion: y=m*(x-x1)+y1
        return f"y = {m}*(x-{punto.get_x()}) + {punto.get_y()}"

    def EcuacionDeLaRecta4(self, a, b, c):
        #ecuacion: a*x+b*y+c=0
        return f"{a}*x + {b}*y + {c} = 0"
    
    def EcuacionDeLaRecta5(self, x0):
        #ecuacion: x=x0
        return f"x = {x0}"
    
    def EcuacionDeLaRecta6(self, y0):
        #ecuacion: y=y0
        return f"y = {y0}"