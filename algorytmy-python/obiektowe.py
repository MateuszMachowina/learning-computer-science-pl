from math import *

class Punkt:
    x = 0
    y = 0
    def przesun_o_wek(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
    def skaluj_OX(self, n):
        self.y *= n
    def przesun_o_kat(self, alfa):
        alfa /=180
        alfa *= 3.1416
        x = self.x
        y = self.y
        self.x = x*cos(alfa) - y*sin(alfa)
        self.y = y*cos(alfa) + x*sin(alfa)
    def zwroc_r(self):
        return sqrt(self.x**2 + self.y**2

punkt1 = Punkt()
print(punkt1.x, punkt1.y)
punkt1.x = 2
punkt1.y = 5
print(punkt1.x, punkt1.y)
punkt1.skaluj_OX(1)
print(punkt1.x, punkt1.y)
punkt1.przesun_o_kat(180)
print(punkt1.x, punkt1.y)

