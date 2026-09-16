'''Q1. Desenvolva um programa que solicite a idade de uma pessoa e classifique-a de acordo com as seguintes regras:
Menor que 0 → Idade inválida
De 0 a 12 anos → Criança
De 13 a 17 anos → Adolescente
De 18 a 59 anos → Adulto
60 anos ou mais → Idoso'''

idade = int(input("Insira sua idade: "))

if 0 <= idade <= 12:
    print("Criança")

elif 13 <= idade <= 17:
    print("Adolescente")

elif 18 <= idade <= 59:
    print("Adulto")

elif idade >= 60:
    print("Idoso")

else:
    print("Idade inválida")
