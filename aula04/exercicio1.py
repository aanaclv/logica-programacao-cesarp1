produto1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input(f"Digite o preço do {produto1}: "))
quantidade1 = int(input(f"Digite a quantidade do {produto1}: "))

produto2 = input("Digite o nome do segundo produto: ")
preco2 = float(input(f"Digite o preço do {produto2}: "))
quantidade2 = int(input(f"Digite a quantidade do {produto2}: "))

produto3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input(f"Digite o preço do {produto3}: "))
quantidade3 = int(input(f"Digite a quantidade do {produto3}: "))    

total1 = preco1 * quantidade1
total2 = preco2 * quantidade2
total3 = preco3 * quantidade3

total_geral = total1 + total2 + total3

print(f'''Produtos comprados e valores: 
{produto1}: {quantidade1} x {preco1} = R${total1:.2f}
{produto2}: {quantidade2} x {preco2} = R${total2:.2f}
{produto3}: {quantidade3} x {preco3} = R${total3:.2f}
Total geral: R${total_geral:.2f}''')