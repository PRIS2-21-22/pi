import math
import punto

class Vector:

    def __init__(self, punto1 ,punto2):
        self.punto1= punto1
        self.punto2 = punto2
    
    def cX(self):
        return self.punto2.get_x() - self.punto1.get_x()

    def cY(self):
        return self.punto2.get_y() - self.punto1.get_y()

    def moduloVector(self):
        return math.sqrt(math.pow(self.cX(),2) + math.pow(self.cY(),2))

    def productovectorialVector(self,vector):
        return self.cX()*vector.cY()- self.cY*vector.cX()

    def ecuacionDeLaRecta(self):
       return f"y = {((self.punto2.get_y()-self.punto1.get_y())/(self.punto2.get_x()-self.punto1.get_x()))}*(x-{self.punto1.get_x()}) + {self.punto1.get_y()}"

    