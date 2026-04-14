# Variáveis do Sistema

cadastro_shopping = input("Possui cadastro no shopping? [sim]/[não]")
cadastro = cadastro_shopping == "sim"
idade = int(input("Idade do cliente: "))
tipo_veiculo = input("Qual tipo de veículo? - [carro], [moto], [caminhonete], [caminhão], [van], [ônibus], [bicicleta]")
tipo_cliente = input("Faz parte do Clube VIP? [sim]/[não]")
vip = tipo_cliente == "sim"

if cadastro == False:
    print("Entrada negada. Necessário cadastro no shopping.")
elif idade < 18:
    print("Entrada negada. Cliente menor de idade.")
elif tipo_veiculo == "caminhão" or "ônibus":
    print("Tipo de veículo não permitido no estacionamento interno.")
elif vip == True:
    print("Entrada autorizada. Seja bem-vindo!")