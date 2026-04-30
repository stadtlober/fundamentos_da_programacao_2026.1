# Saldo inicial da conta
saldo = 1000.00

# Lista para armazenar histórico de transações
historico = []

# Loop principal do sistema (mantém o caixa eletrônico rodando)
while True:
    print("\n🏧  --- Bem-vindo ao Caixa Eletrônico ---")
    print("\n--- Menu Principal ---")
    print("1️⃣  Depositar")
    print("2️⃣  Sacar")
    print("3️⃣  Ver Saldo")
    print("4️⃣  Ver Historico")
    print("5️⃣  Sair")

    # Captura opção do usuário
    opcao = input("\n↪️  Escolha uma opção:")

# ---------------- DEPÓSITO ----------------
    if opcao == "1":
        # Solicita valor de depósito
        deposito = float(input("\n➡️  Digite o valor a ser depositado: R$"))

        # Atualiza saldo
        saldo = saldo + deposito

        # Registra no histórico
        historico.append(f"➕  Deposito: +R${deposito}")

        print("\n✅  Deposito realizado com sucesso!")
        print(f"💵  Saldo atual: R${saldo}")
        print("\n🔙  Retornando ao menu...")

# ---------------- SAQUE ----------------
    elif opcao == "2":

        # Loop para permitir tentativa de saque até sucesso ou desistência
        while True:

            # Solicita valor de saque
            saque = float(input("➡️  Digite o valor a ser sacado: R$"))

            # Verifica se há saldo suficiente
            if saque <= saldo:
                saldo = saldo - saque
                historico.append(f"➖  Saque: -R${saque}")

                print("\n✅  Saque realizado com sucesso!")
                print(f"💵  Saldo atual: R${saldo}")
                print("\n🔙  Retornando ao menu...")

                break # sai do loop de saque
            
            else:
                # Caso saldo seja insuficiente
                print("\n🚫  Saldo insuficiente.")
                print(f"💵  Saldo disponivel: R${saldo}")
                print("-----")

                # Opções de correção
                print(f"1️⃣  Tentar novamente")
                print(f"2️⃣  Voltar ao menu")

                opcao_saque = input("↪️  Escolha uma opcao:")

                if opcao_saque == "1":
                    continue # volta a pedir saque
                
                elif opcao_saque == "2":
                    print("🔙  Retornando ao menu...")
                    break # sai do loop de saque

# ---------------- VER SALDO ----------------
    elif opcao == "3":
        print(f"\n💵  Seu saldo atual e: R${saldo}")
        print("🔙  Retornando ao menu...")

# ---------------- HISTÓRICO ----------------
    elif opcao == "4":
        print("📄  Historico de Transacoes\n")

        # Percorre todas as transações registradas
        for item in historico:
            print(item)

        print("\n🔙  Retornando ao menu...")

# ---------------- SAIR ----------------
    elif opcao == "5":
        print("\n🔒 Encerrando sessão...")
        print("👋 Até logo!")
        break # encerra o loop principal