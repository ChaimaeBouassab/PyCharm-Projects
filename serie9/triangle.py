from Point import Point
class Triangle:
    def __init__(self,A,B):
        self.a=A
        self.b=B
    def longueur(self):
        return self.a.x-self.b.x
    def largeur(self):
        return self.a.y-self.b.y
    def tester(self):
        return self.longueur()==self.largeur()
    def afficher(self):
        print("poooo=",self.a,"pkkkk=",self.b)


A=Point(3,5)
F=Point(1,0)
c=Triangle(A,6)
h=c.largeur()
h.afficher()

