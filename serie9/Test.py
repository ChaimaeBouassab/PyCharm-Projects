'''from Point import Point
A=Point(2,4)
B=Point(3,1)
A.afficher()
h=A.distance(B)
k=A.milieu(B)
k.afficher()
h.afficher()'''

from cercle import Circle
from Point import Point
A=Point(3,5)
F=Point(1,0)
c=Circle(A,6)
c.affichage()
b=c.appartient(F)
if b==True:
    print(" il appartient")
else:
    print("il n appartient pas")




