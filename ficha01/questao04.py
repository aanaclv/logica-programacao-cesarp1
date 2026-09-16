'''Uma instituição financeira deseja analisar solicitações de empréstimo.
Solicite:
Idade;
Salário;
Tempo de trabalho em anos;
Valor solicitado.
Utilize as regras:
Menor de 18 anos → Empréstimo não permitido
Salário menor que R$ 1.500 → Renda insuficiente
Tempo de trabalho menor que 1 ano → Tempo de trabalho insuficiente
Valor solicitado superior a 10 vezes o salário → Valor solicitado muito alto
Caso contrário → Empréstimo pré-aprovado
O programa deverá avaliar as condições na ordem adequada.'''

idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário: "))
tempo_trabalho_anos = int(input("Insira seu tempo de trabalho em anos: "))
valor_solicitado = float(input("Insira o valor solicitado: "))


if idade >= 18 and salario >= 1500 and tempo_trabalho_anos >= 1 and valor_solicitado < salario*10:
    print("Empréstimo pré-aprovado")

else:
    if idade < 18:
        print("Empréstimo não permitido")

    if salario < 1500:
        print("Renda insuficiente")

    if tempo_trabalho_anos < 1:
        print("Tempo de trabalho insuficiente")

    if valor_solicitado > salario*10:
        print("Valor solicitado muito alto")
