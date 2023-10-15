from Point import Point
class Carre:
    def __init__(self,A,reel):
        self.a=A
        self.b=reel
    def surface(self):
        return self.b*self.b
    def perimetre(self):
        return self.b*4
