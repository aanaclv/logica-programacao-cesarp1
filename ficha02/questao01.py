'''Q1. Desenvolva um programa em Python que solicite ao usuário um número inteiro positivo N e, utilizando a estrutura de repetição for, apresente na tela todos os números inteiros de 1 até N.
Exemplo: Se o usuário informar 5, o programa deverá apresentar:
1
2
3
4
5'''

n = int(input("Insira um número: "))

for i in range(1,n+1):
    print(i)