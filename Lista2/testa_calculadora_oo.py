from calculadora_oo import Calculadora
def teste():
    h = Calculadora()
    print(h.somar(7,8))
    print(h.subtrair(100,5))
    print(h.multiplicar(12,57))
    print(h.dividir(18,6))
    print(h.somar(10))
    print(h.subtrair(6))
    print(h.multiplicar(12))
    print(h.dividir(96))

if __name__ == "__main__":
    teste()