'''Uma empresa deseja classificar o desempenho de seus funcionários.
Solicite:
Nota de produtividade;
Nota de qualidade;
Percentual de presença.
Calcule a média das duas notas.
Classifique:
Presença < 75% → Desempenho comprometido por baixa frequência
Média ≥ 9 e presença ≥ 90% → Excelente
Média ≥ 7 e presença ≥ 85% → Bom
Média ≥ 5 e presença ≥ 75% → Regular
Caso contrário → Insatisfatório'''

nota_produtividade = int(input("Insira a nota da produtividade: "))
nota_qualidade = int(input("Insira a nota de qualidade: "))
percentual_presenca = int(input("Insira o percentual de presença: "))
media = (nota_produtividade+nota_qualidade)/2

if percentual_presenca < 75:
    print("Desempenho comprometido por baixa frequência")

elif media > 9 and percentual_presenca > 90:
    print("Excelente")

elif media >= 7 and percentual_presenca >= 85:
    print("Bom")

elif media >= 5 and percentual_presenca >= 75:
    print("Regular")

else:
    print("Insatisfatório")