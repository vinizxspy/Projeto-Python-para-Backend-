def contar_negativos(lista):
    contador = 0

    for numero in lista:
        if numero < 0:
            contador += 1

    return contador


valores = [10, -2, 7, -5, -9, 3]
print(contar_negativos(valores))