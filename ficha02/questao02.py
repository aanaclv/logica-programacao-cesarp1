'''Q2. Escreva um programa que solicite ao usuário um número inteiro positivo N e utilize uma estrutura de repetição for para exibir todos os números pares entre 1 e N.
Ao final, o programa deverá informar também quantos números pares foram encontrados.
Exemplo: Para N = 10:
Números pares:
2
4
6
8
10'''

n = int(input("insira um número: "))

for i in range(2,n+1,2):
    print(i)