#2
#Múltiplos
#Função que retorna lista com todos os múltiplos de 3 entre 1 e N.

def multiplos(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i)

numero = int(input("Digite um número: "))
multiplos(numero)