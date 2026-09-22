'''Q9. Desenvolva um programa que permita cadastrar as notas de vários estudantes.
O programa deverá utilizar a estrutura while para solicitar continuamente uma nota. A entrada deverá ser encerrada quando o usuário informar o valor -1.
Para cada nota válida, o programa deverá verificar se o estudante foi:
Aprovado: nota maior ou igual a 7;
Recuperação: nota maior ou igual a 5 e menor que 7;
Reprovado: nota menor que 5.
Ao final, apresente:
quantidade de estudantes aprovados;
quantidade de estudantes em recuperação;
quantidade de estudantes reprovados;
quantidade total de estudantes cadastrados.
O valor -1 deve ser utilizado apenas para encerrar a entrada e não deve ser considerado uma nota.'''
nota = 0
aprovados = 0
recuperacao = 0
reprovados = 0
total_estudantes = 0

while nota != -1:
    nota = int(input("insira a nota: "))
    if nota > 0 and nota <= 10:
        if nota >= 7:
            aprovados += 1
        if nota >= 5 and nota < 7:
            recuperacao +=1
        if nota < 5:
            reprovados += 1
    total_estudantes = aprovados + reprovados + recuperacao

print(f'''quantidade de estudantes aprovados: {aprovados}
quantidade de estudantes em recuperação: {recuperacao}
quantidade de estudantes reprovados: {reprovados}
quantidade total de estudantes cadastrados: {total_estudantes}
''')
