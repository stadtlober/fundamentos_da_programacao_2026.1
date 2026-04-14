# Variáveis do Sistema

idade = int(input("Idade do aluno: "))
nota = float(input("Nota obtida na prova: "))
while nota > 10.0:
    print("Informe uma nota válida.")
    nota = float(input("Digite novamente: "))
frequencia = float(input("Frequência do aluno (%): "))
while frequencia > 100:
    print("Informe um número de frequência válido.")
    frequencia = float(input("Digite novamente: "))

# Análise de Matrícula

if idade < 18:
    print("Matrícula negada. Aluno menor de idade.")
elif nota >= 9:
    print("Matrícula aprovada automaticamente.")
elif nota < 6:
    print("Matrícula negada. Nota menor que 6.")
elif frequencia < 75:
    print("Matrícula negada. Frequência menor que 75%.")
else:
    print("Matrícula aprovada.")