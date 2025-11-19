def cambio(N):
    monedas = [25, 10, 5, 1]
    resultado = {}

    for m in monedas:
        resultado[m] = N // m
        N %= m

    return resultado

# Ejemplo
N = int(input("Ingresa N: "))
print(cambio(N))
