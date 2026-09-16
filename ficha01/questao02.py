'''Q2. Uma empresa precisa classificar seus produtos de acordo com o preço e a quantidade disponível.
Solicite:
Preço do produto;
Quantidade em estoque.
Classifique o produto:
Preço menor ou igual a zero → Preço inválido
Quantidade menor que zero → Quantidade inválida
Preço acima de R$ 1.000 e estoque menor que 5 → Produto caro com estoque crítico
Preço acima de R$ 1.000 e estoque entre 5 e 20 → Produto caro com estoque normal
Preço acima de R$ 1.000 e estoque acima de 20 → Produto caro com estoque alto
Preço até R$ 1.000 e estoque menor que 5 → Estoque crítico
Caso contrário → Estoque normal'''

preco_produto = float(input("Insira o preço do produto: "))
quantidade_estoque = int(input("Insira a quantidade em estoque: "))

if preco_produto <= 0:
    print("Preço inválido")


if quantidade_estoque < 0:
    print("Quantidade inválida")

if preco_produto > 1000 and quantidade_estoque < 5:
    print("Produto caro com estoque crítico")
elif preco_produto > 1000 and  5 <= quantidade_estoque <= 20:
    print("Produto caro com estoque normal")
elif preco_produto > 1000 and quantidade_estoque > 20:
    print("Produto caro com estoque alto")
elif preco_produto <= 1000 and quantidade_estoque < 5:
    print("Estoque crítico")
else:
    print("Estoque normal")
