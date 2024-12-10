#calculadora modularizada
acumulador = 0.0
def sum(a, b = None ):
    global acumulador
    if b == None:
        return acumulador + a
    acumulador = a + b
    return a + b

def sub(a, b = None ):
    global acumulador
    if b == None:
        return acumulador - a
    acumulador = a - b
    return a - b

def mult(a, b = None ):
    global acumulador
    if b == None:
        return acumulador * a
    acumulador = a * b
    return a * b

def div(a, b = None ):
    global acumulador
    if b == None:
        return acumulador / a
    acumulador = a / b
    return a / b
