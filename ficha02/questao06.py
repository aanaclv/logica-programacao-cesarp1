'''
Q6.Desenvolva um programa que solicite ao usuário uma senha numérica.
O programa deverá utilizar a estrutura de repetição while para permitir que o usuário tente informar a senha corretamente.
Considere que a senha correta seja:
1234
O programa deverá continuar solicitando a senha enquanto o usuário não informar o valor correto.
Quando a senha estiver correta, apresente:
Acesso autorizado!
'''
login =""
senha = 1234

while login != senha:
    login = int(input("digite a senha: "))
    if login != senha:
        print("incorreto. digite novamente: ")
print("aprovado")
