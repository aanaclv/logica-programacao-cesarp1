'''Q9. Desenvolva um programa que solicite ao usuário uma quantidade N de números inteiros. Em seguida, utilizando uma estrutura de repetição for, leia os N valores e determine:
o maior número informado;
o menor número informado;
a diferença entre o maior e o menor número.
Exemplo:
Quantidade de números: 5

Digite o 1º número: 12
Digite o 2º número: 7
Digite o 3º número: 25
Digite o 4º número: 4
Digite o 5º número: 18

Maior número: 25
Menor número: 4
Diferença: 21
'''
quantidade = int(input("insira a quantidade de números inteiros: "))

for i in range(quantidade):
    n = int(input(f"insira o {i+1} número: "))
    if i == 0:
            maior_valor = n
            menor_valor = n
    else:
        if n > maior_valor:
            maior_valor = n
    
        if n < menor_valor:
                menor_valor = n
    diferenca = maior_valor - menor_valor

print(f'''Maior valor:{maior_valor}
Menor valor: {menor_valor}
Diferença: {diferenca}''')
