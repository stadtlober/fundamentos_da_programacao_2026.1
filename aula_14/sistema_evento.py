while True:
    start = input("Digite seu nome: ")
    if start == "sair":
     print("Encerrando...")
     break
    elif start != "sair":
       idade = int(input("Digite sua idade: "))
       convite = input("Possui convite? [S]/[N] ")
    if idade < 16:
      print("Entrada negada")
    if idade >= 16 and convite == "S":
      print("Entrada permitida")
    if convite == "N":
      print("Entrada negada")