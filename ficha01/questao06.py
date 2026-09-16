'''Q7. Desenvolva um programa que apresente o seguinte menu:
1 - Cadastrar aluno
2 - Consultar aluno
3 - Alterar aluno
4 - Excluir aluno
5 - Listar alunos
6 - Sair
O usuário deverá informar uma opção.
Utilize obrigatoriamente a estrutura match para executar a ação correspondente.
Caso seja informada uma opção diferente de 1 a 6, apresente:
Opção inválida.'''

print('''
MENU
1 - Cadastrar aluno
2 - Consultar aluno
3 - Alterar aluno
4 - Excluir aluno
5 - Listar alunos
6 - Sair
''')

opcao = int(input("Insira uma opção: "))

match opcao:
    case 1:
        print("Cadastrando aluno...")
    case 2:
        print("Consultando aluno..")
    case 3:
        print("Alterando aluno..")
    case 4:
        print("Excluindo alunos..")
    case 5:
        print("Listando alunos..")
    case 6:
        print("Encerrando programa...")
    case _:
        print("Opção inválida")