import math

class Poligono:
    def __init__(self):
        self.pontos = []

    def area(self):
        total = 0
        n = len(self.pontos)
        for i in range(n):
            x0 = self.pontos[i].x
            y0 = self.pontos[i].y
            x1 = self.pontos[(i+1)%n].x
            y1 = self.pontos[(i+1)%n].y
            total+=(x0*y1-x1*y0)
        return total/2

    def perimetro(self):
        total = 0
        n = len(self.pontos)
        for i in range(n):
            x1 = self.pontos[(i+1)%n].x
            y1 = self.pontos[(i+1)%n].y
            x0 = self.pontos[i%n].x
            y0 = self.pontos[i%n].y
            total += math.sqrt((x1-x0)**2 + (y1-y0)**2)
        return total

    def addPonto(self, ponto):
        self.pontos.append(ponto)

    def __str__(self):
        return f"Área atual do polígono: {self.area()} - Perímetro atual do polígono: {self.perimetro()}."
