class Point:
    def init(self, x, y):
        self.__x = x
        self.__y = y

    def deplace(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def affiche(self):
        print("abscisse =", self.x, "ordonnee =", self.y)


a = Point(2, 4)
a.affiche()
a.deplace(1, 3)
a.affiche()
