#receba 5 valores e diga o maior entre eles

for i in range (5):
    if i < 5:
        valor = int (input("digite um valor: "))

        if i == 0:
            maior_valor = valor

        if valor > maior_valor:
            maior_valor = valor

print(f"O maior valor é: {maior_valor}")
