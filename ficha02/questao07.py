'''Q7. Escreva um programa que solicite ao usuário 10 números inteiros. Utilize uma estrutura de repetição for para realizar as entradas e, ao final, informe:
quantos números positivos foram digitados;
quantos números negativos foram digitados;
quantos números iguais a zero foram digitados.
Exemplo de resultado:
Quantidade de positivos: 4
Quantidade de negativos: 5
Quantidade de zeros: 1
'''
positivos = 0
negativos = 0
zeros = 0

for i in range(10):
    n = int(input(f"insira o {i+1} número: "))

    if n > 0:
        positivos += 1
    if n < 0:
        negativos += 1
    if n == 0:
        zeros += 1

print(f'''Quantidade de positivos: {positivos}
Quantidade de negativos: {negativos}
Quantidade de zeros: {zeros}
''')
        
