
def divisao_inteligente(func):
    def wrapper(x,y):
        print(f"Dividindo: {x}/{y}")
        if y == 0.0:
            return "ERRO_DIV_POR_ZERO"
        else:
            return func(x,y)
    return wrapper

@divisao_inteligente
def dividir(operando_a,operando_b) -> float:
    return operando_a/operando_b

if __name__ == "__main__":
    print(f"-> Resultado: {dividir(3,3)}")
    print(f"-> Resultado: {dividir(3,0)}")