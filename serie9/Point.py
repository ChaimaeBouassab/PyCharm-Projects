import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def distance(self,p):
        d=math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
        return p
    def afficher(self):
        print("abscisse=",self.x,"ordonnee=",self.y)
    def milieu(self,p):
        M=Point()
        M.x= (self.x+p.x)/2
        M.y=(self.y+p.y)/2
        return M

