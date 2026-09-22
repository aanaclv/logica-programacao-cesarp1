'''Q4. Elabore um programa que solicite ao usuário um número inteiro e apresente sua tabuada de 1 a 10.
O programa deverá utilizar obrigatoriamente a estrutura de repetição for.
Exemplo:
Digite um número: 7

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70'''

n = int(input("insira o valor que deseja da tabuada: "))

for i in range(1,11):
    print(f"{n}x{i}={n*i}")
