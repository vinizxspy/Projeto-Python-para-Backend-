#Média sem extremos
#Leia 10 notas, elimine a maior e menor, calcule média
soma = 0

for i in range(10):
    nota = float (input("digite a nota: "))

    soma += nota
    if i == 0:
        maior_nota = nota
        menor_nota = nota
    
    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

    media = (soma - maior_nota - menor_nota) / 8

print (f"a média é: {media}")
print (f"a maior nota é : {maior_nota}")
print (f"a menor nota é : {menor_nota}")