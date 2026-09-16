'''Q3. Uma universidade deseja verificar se um estudante pode receber uma bolsa.
Solicite:
Média acadêmica;
Percentual de frequência;
Renda familiar;
Se o aluno possui outra bolsa (S ou N).
Regras:
O aluno será elegível se:
Média ≥ 7;
Frequência ≥ 75%;
Renda familiar ≤ R$ 3.000;
Não possuir outra bolsa.
Caso contrário, informe o motivo:
Média insuficiente;
Frequência insuficiente;
Renda acima do limite;
Já possui outra bolsa.'''

media_academica = float(input("Insira sua média acadêmica: "))
percentual_frequencia = float(input("Insira seu percentual de frequência: "))
renda_familiar = float(input("Insira sua renda familiar: "))
possui_bolsa = input("Possui bolsa? (S/N): ")

if media_academica >= 7 and percentual_frequencia >= 75 and renda_familiar <= 3000 and possui_bolsa == "N":
    print("Bolsa aprovada")

else:
    if media_academica < 7:
        print("Média insuficiente")
    if percentual_frequencia < 75:
        print("Frequência insuficiente")
    if renda_familiar > 3000:
        print("Renda acima do limite")
    if possui_bolsa == "S":
        print("Já possui outra bolsa")