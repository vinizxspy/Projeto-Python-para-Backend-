def soma_pares(lista):
    soma = 0

    for numero in lista:
        if numero % 2 == 0:
            soma += numero

    return soma


valores = [5, 8, 2, 9, 4, 7]
print(soma_pares(valores))