'''Uma instituição de ensino deseja criar um sistema para verificar a situação de matrícula de um aluno.
Solicite:
Idade;
Média do aluno;
Percentual de frequência;
Tipo de curso:
1 – Graduação
2 – Técnico
3 – Pós-graduação
Utilize match para identificar o curso e if/elif/else para determinar a situação.
Regras:Graduação
Média ≥ 7 e frequência ≥ 75% → Aprovado
Média ≥ 5 e frequência ≥ 75% → Recuperação
Caso contrário → Reprovado
Técnico
Média ≥ 6 e frequência ≥ 75% → Aprovado
Média ≥ 4 e frequência ≥ 75% → Recuperação
Caso contrário → Reprovado
Pós-graduação
Média ≥ 7 e frequência ≥ 75% → Aprovado
Caso contrário → Reprovado
Se a frequência for inferior a 75%, o aluno deverá ser reprovado por falta, independentemente do curso ou da média.'''

idade = int(input("Insira a idade: "))
media_aluno = float(input("Insira a média do aluno: "))
percentual_frequencia = int(input("Insira o percentual de frequência: "))
tipo_curso = int(input("Insira o tipo de curso (1 - graduação, 2 - técnico e 3 - pós-graduação): "))


match tipo_curso:
    case 1:
        if percentual_frequencia < 75:
            print("reprovado por falta, independente do curso ou da matéria")
        elif media_aluno >= 7 and percentual_frequencia >= 75:
            print("aprovado")
        elif media_aluno >= 5 and percentual_frequencia >= 75:
            print("recuperação")
        else:
            print("reprovado")

    case 2:
        if percentual_frequencia < 75:
            print("reprovado por falta, independente do curso ou da matéria")        
        elif media_aluno >= 5 and percentual_frequencia >= 75:
            print("aprovado")
        elif media_aluno >= 4 and percentual_frequencia >= 75:
            print("recuperação")
        else:
            print("reprovado")

    case 3:
        if percentual_frequencia < 75:
            print("reprovado por falta, independente do curso ou da matéria")        
        elif media_aluno >= 7 and percentual_frequencia >= 75:
            print("aprovado")
        else:
            print("reprovado")