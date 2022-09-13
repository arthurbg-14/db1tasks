def fatorial(int):
    resultado = 1
    for i in range(int):
        resultado*=(i+1)
    return resultado

print(fatorial(1000))