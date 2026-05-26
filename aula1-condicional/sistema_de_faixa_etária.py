#Este exercício aplica a estrutura condicional 
# if-elif-else 
# para classificar a entrada do usuário em diferentes categorias
#Categorias
#Criança (0-12), Adolescente (13-17), Adulto (18+)

idade = int(input("digite sua idade: "))

if idade <= 12:
    print ("você é criança")
elif idade >= 13 and idade <= 17:
    print ("você é adolescente")
else:
    if idade >= 18:
        print ("você é adulto")