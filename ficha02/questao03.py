'''Q3. Desenvolva um programa que solicite ao usuário um número inteiro positivo N e calcule a soma de todos os números inteiros de 1 até N, utilizando a estrutura de repetição for.
Exemplo:
Digite um número: 5

Soma = 15
Pois:
1 + 2 + 3 + 4 + 5 = 15'''

n = int(input("digite um número: "))
soma = 0
for i in range(n+1):
    soma += i

print(f"soma: {soma}")