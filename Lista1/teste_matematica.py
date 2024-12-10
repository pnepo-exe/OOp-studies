from matematica import *
from matematica.estatistica import media

def teste():
    h = [2, 4, 5, 6, 7, 8, 9, 10, 12, 17]
    print(soma(2,3))
    print(sub(10,5))
    print(area_circulo(10))
    print(area_retangulo(30,40))
    print(media.media_simples(h))

if __name__ == "__main__":
    teste()