'''Q10. Desenvolva um programa que simule um caixa eletrônico utilizando a estrutura de repetição while.
O programa deverá apresentar um menu com as seguintes opções:
1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Sair
Considere que o saldo inicial seja de R$ 1.000,00.
O programa deverá:
permitir consultar o saldo;
permitir realizar depósitos;
permitir realizar saques somente quando houver saldo suficiente;
informar quando o valor do saque for superior ao saldo disponível;
continuar exibindo o menu até que o usuário escolha a opção 4 – Sair;
apresentar uma mensagem de encerramento ao finalizar o programa.'''

saldo = 1000

opcao = 0

while opcao != 4:

    opcao = int(input('''
1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Sair
Escolha uma opção: '''))

    if opcao == 1:
        print(f"saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        deposito = float(input("quanto deseja depositar? R$ "))
        saldo += deposito
        print(f"depósito realizado. Novo saldo: R$ {saldo:.2f}")

    elif opcao == 3:
        saque = float(input("quanto deseja sacar? R$ "))

        if saque <= saldo:
            saldo -= saque
            print(f"saque realizado. Novo saldo: R$ {saldo:.2f}")
        else:
            print("valor do saque superior ao saldo disponível.")

    elif opcao == 4:
        print("encerrando programa...")

    else:
        print("opção inválida!")

print("Programa finalizado.")