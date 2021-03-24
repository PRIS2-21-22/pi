import math
import punto

class Vector:

    def __init__(self, punto1 ,punto2):
        self.punto1= punto1
        self.punto2 = punto2

    
    def c_x(self):
        return self.punto2.get_x() - self.punto1.get_x()

    def c_y(self):
        return self.punto2.get_y() - self.punto1.get_y()

    def modulo_vector(self):
        return math.sqrt(math.pow(self.cX(),2) + math.pow(self.cY(),2))

    def producto_vectorial_vector(self,vector):
        return self.cX()*vector.cY()- self.cY*vector.cX()

    def ecuacion_de_la_recta(self):
        #ecuacion: y=[(y2-y1)/(x2-x1)]*(x-x1)+y1
        return f"y = {((self.punto2.get_y()-self.punto1.get_y())/(self.punto2.get_x()-self.punto1.get_x()))}*(x-{self.punto1.get_x()}) + {self.punto1.get_y()}"

    def ecuacion_de_la_recta_2(self, m, b):
        #ecuacion: y = mx+b
        return f"y = {m}*x + {b}"
    
    def ecuacion_de_la_recta_3(self, m, punto):
        #ecuacion: y=m*(x-x1)+y1
        return f"y = {m}*(x-{punto.get_x()}) + {punto.get_y()}"

    def ecuacion_de_la_recta_4(self, a, b, c):
        #ecuacion: a*x+b*y+c=0
        return f"{a}*x + {b}*y + {c} = 0"
    
    def ecuacion_de_la_recta_5(self, x0):
        #ecuacion: x=x0
        return f"x = {x0}"
    
    def ecuacion_de_la_recta_6(self, y0):
        #ecuacion: y=y0
        return f"y = {y0}"