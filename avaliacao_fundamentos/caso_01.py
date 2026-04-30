# Solicita a quantidade de alunos que serão cadastrados
numero_alunos = int(input("Quantos alunos serão cadastrados? "))

# Lista que irá armazenar todos os alunos
alunos = []

# Loop que roda enquanto ainda houver alunos para cadastrar
while numero_alunos > 0:

    # ---------------- DADOS DO ALUNO ----------------
    # Nome do aluno
    nome = input("👤 Nome do aluno: ")

    # Lista de notas do aluno (3 avaliações)
    notas = [
        float(input("➡️  Digite a nota da Avaliação 1:")),
        float(input("➡️  Digite a nota da Avaliação 2:")),
        float(input("➡️  Digite a nota da Avaliação 3:"))
    ]

    # ---------------- CÁLCULO DA MÉDIA ----------------
    # Soma as notas e divide pela quantidade
    media = sum(notas) / len(notas)

    # Arredonda a média para 2 casas decimais
    media = round(media, 2)

    # ---------------- SITUAÇÃO DO ALUNO ----------------
    # Define a situação com base na média
    if media >= 7:
        situacao = "✅ Aprovado"
    elif media >= 5:
        situacao = "‼️ Recuperação"
    else:
        situacao = "🚫 Reprovado"

    # ---------------- ESTRUTURA DO ALUNO ----------------
    # Cria uma lista com todas as informações do aluno
    aluno = [nome, notas, media, situacao]

    # Adiciona o aluno na lista principal
    alunos.append(aluno)

    # Reduz o contador de alunos restantes
    numero_alunos -= 1

    print("\n✔️ Aluno cadastrado com sucesso!")
    print("-----")

# ---------------- EXIBIÇÃO FINAL ----------------
print("📚 Resumo da turma:\n")

# Percorre todos os alunos cadastrados
for aluno in alunos:
    print(f"👤 Aluno: {aluno[0]}")
    print(f"➡️ Notas: {aluno[1]}")
    print(f"📊 Média: {aluno[2]}")
    print(f"🎯 Situação: {aluno[3]}")
    print("-----")