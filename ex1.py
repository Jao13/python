media_final = int(input("Sua média final: "))
presenca = int(input("Porcentagem de presença de um alun: "))

if (media_final >= 7) and presenca >= 75:
    print("Aprovado")
else:
    print("Reprovado")