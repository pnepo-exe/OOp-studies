class Calculadora:
    def __init__(self):
        self.acumulardor = 0.0
    def somar(self, operando_a ,operando_b = None):
        if operando_b == None:
            return self.acumulardor + operando_a
        self.acumulardor = operando_a + operando_b
        return operando_a + operando_b
    def subtrair(self,operando_a,operando_b = None):
        if operando_b == None:
            return self.acumulardor - operando_a
        self.acumulardor = operando_a - operando_b
        return operando_a - operando_b
    def multiplicar(self,operando_a,operando_b = None):
        if operando_b == None:
            return self.acumulardor * operando_a
        self.acumulardor = operando_a * operando_b
        return operando_a * operando_b
    def dividir(self,operando_a,operando_b = None):
        if operando_b == None:
            return self.acumulardor / operando_a
        self.acumulardor = operando_a / operando_b
        return operando_a / operando_b