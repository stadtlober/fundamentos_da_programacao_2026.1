# Variáveis do Sistema

idade = int(input("Informe sua idade: "))
salario = float(input("Informe seu salário: ").replace(",", "."))
tempo_trabalho = int(input("Informe seu tempo de trabalho: "))
valor_emprestimo = float(input("Qual valor do empréstimo desejado? "))
taxa = 0.02
numero_parcelas = int(input("Qual número de parcelas desejado? "))
valor_parcela = int(valor_emprestimo * (taxa * (1 + taxa)**numero_parcelas) / ((1 + taxa)**numero_parcelas - 1))

# Condições

# Negação Automática
# Se parcela > 30% do salário → empréstimo negado

# Aprovação automática
# Se o salário for maior ou igual a R$ 5000 → o empréstimo é aprovado automaticamente

# Negação Automática
# Se a idade for menor que 18 → o empréstimo é negado automaticamente

# Verificação de Dados
print(f"O cliente tem {idade}, salário de R$ {salario} e {tempo_trabalho} anos de trabalho. O empréstimo desejado é no valor de R$ {valor_emprestimo}, em {numero_parcelas} parcelas de R$ {valor_parcela}")

# Análise da Solicitação
if idade < 18:
    print(f"Pedidos de empréstimo só podem ser realizados por clientes maiores de idade.")
elif valor_parcela > 0.3 * salario:
    print(f"Seu empréstimo foi negado pois a parcela compromete mais de 30% da sua renda.")
elif salario >= 5000:
    print(f"Empréstimo aprovado!")
elif idade >= 18 and salario >= 2000 and tempo >= 2:
     print(f"Seu pedido de empréstimo está em análise!")
else:
    print("Seu empréstimo foi negado pois você não atende as condições básicas necessárias.")
