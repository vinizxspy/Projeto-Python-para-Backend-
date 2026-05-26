#O desafio é criar um programa completo 
# que receba as notas, calcule a média e 
# classifique o resultado conforme os critérios.

#Reprovado 0-4
#Recuperação 5-7
#Aprovado 8-10

nota1 = int(input("digite a primeira nota: "))
nota2 = int(input("digite a segunda nota: "))
nota3 = int(input("digite a terceira nota: "))

media = nota1 + nota2 + nota3 /3

if media <= 4:
    print ("o aluno está reprovado")
elif media >= 5 and media <= 7:
    print("o aluno está de recuperação")
elif media >= 8:
    print("o aluno está aprovado")