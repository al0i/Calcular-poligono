from ponto import Ponto
from poligono import Poligono

def main(x,y):
    ponto = Ponto(x,y)
    poligono.addPonto(ponto)
    return poligono.__str__()

poligono = Poligono()
while True:
    x = input("Digite X (ENTER para parar): ")
    if x == "":
        break    
    y = float(input("Digite Y: "))
    print(main(x,y))