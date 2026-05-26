contador = 0
continuar = 1

while continuar == 1:
    print("OI")
    
    contador += 1
    
    continuar = int(input("Digite 1 para continuar e 2 para interromper: "))

print(f"Programa encerrado.")
print(f"OI apareceu {contador} vezes.")