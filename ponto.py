class Ponto:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f'({self.x:.2f}, {self.y:.2f})'