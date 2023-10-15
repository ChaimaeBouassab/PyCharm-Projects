from Point import Point
import math
class Circle:
    def __init__(self,O,R):
        self.r=R
        self.o=O
    def appartient(self,p):
        d=self.o.distance(p)
        return d==self.r

    def affichage(self):
        print("rayon=",self.r)
        self.o.afficher()
    def confondu(self,p,t):
        c1=Circle()
        if self.r==t.r and self.o.x==p.o.x and self.o.y==p.o.y:
            print("confondus")
        else:
            print("NON confondus")




