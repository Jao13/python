nota = int(input("Digite sua nota: "))
faltas = int(input("Quantas faltas vc teve: "))

if (nota >= 7) and faltas >= 75:
    print("Aprovado!")
else:
    print("Reprovado!")