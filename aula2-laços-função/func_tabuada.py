#1
#Tabuada
#Crie uma função que receba um número e imprima sua tabuada de 1 a 10.

def tabuada(n):
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

n = int(input("Digite um número: "))
tabuada(n)