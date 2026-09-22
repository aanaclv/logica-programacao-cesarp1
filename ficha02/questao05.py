'''Q5. Desenvolva um programa que solicite inicialmente a quantidade de números que serão informados pelo usuário. Em seguida, utilize uma estrutura de repetição for para solicitar cada um dos valores.
Ao final, o programa deverá apresentar:
a soma dos valores informados;
a média dos valores;
o maior valor informado;
o menor valor informado.
'''

quantidade = int(input("insira a quantidade de números: "))
soma = 0
maior_valor = 0
menor_valor = 0

for i in range(quantidade):
    n = int(input(f"insira o {i+1} número: "))
    soma += n

    if i == 0:
        maior_valor = n
        menor_valor = n
    else:
        if n > maior_valor:
            maior_valor = n

        if n < menor_valor:
                menor_valor = n

media = soma/quantidade



print(f'''Soma dos valores: {soma}
Média dos valores: {media}
Maior valor: {maior_valor}
Menor valor informado: {menor_valor} ''')
        