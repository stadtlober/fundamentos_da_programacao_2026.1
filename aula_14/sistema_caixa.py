valor = " "
total = 0
quantidade = 0
media = " "
while True:
    valor = int(input("Digite o valor do produto: "))
    if valor == 0:
        if total > 100:
            total_desconto = total * 0.9
            print(f"Total:{total_desconto}")
        else:
            print(f"Total:{total}")
        print(f"Quantidade:{quantidade}")
        print(f"Media: {media}")
        break
    else:
        total += valor
        quantidade += 1
        media = total / quantidade


        