# Variáveis da pizzaria
FRETE = 2 # Constante Fake
pizza_sabor = input("Informa o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]:") 
pizza_tamanho = input("Informa o tamanho da pizza - [pequena], [média], [grande]:")
dia_semana = input("Informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]:")

print(f"O sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")

# Promoções -> Estruturas Condicionais

# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito.

# Comprando uma pizza de cabalebra tamanho médio, em qualquer dia, o frete é grátis.

# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos.

if dia_semana == "sábado":
    print(f"🍕 Pedido aceito com sucesso!")
    print(f"O refri é hoje é por conta da casa.")
elif dia_semana == "domingo": 
    print(f"🍕 Pedido aceito com sucesso!")
    print(f"O refri e o frete hoje é por conta da casa.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "médio":
    print(f"🍕 Pedido aceito com sucesso!")
    print(f"O frete hoje é por conta da casa.")
