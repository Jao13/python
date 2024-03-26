nota1 = int(input("Degite a primeira nota: "))
nota2 = int(input("Degite a segunda nota: "))
nota3 = int(input("Degite a terceira nota: "))

if nota1 > nota2 and nota1 > nota3:
    if nota2 > nota3:
        print(f"Ordem decrescente: {nota1}, {nota2}, {nota3}")
        input("\n Pressione qualquer tecla...")
    else:
        print(f"Ordem decrescente: {nota1}, {nota3}, {nota2}")
        input("\n Pressione qualquer tecla...")

if nota2 > nota1 and nota2 > nota3:
    if nota3 > nota1:
        print(f"Ordem decrescente: {nota2}, {nota1}, {nota3}")
        input("\n Pressione qualquer tecla...")
    else:
        print(f"Ordem decrescente: {nota2}, {nota3}, {nota1}")
        input("\n Pressione qualquer tecla...")

if nota3 > nota1 and nota3 > nota2:
    if nota1 > nota2:
        print(f"Ordem decrescente: {nota3}, {nota1}, {nota2}")
        input("\n Pressione qualquer tecla...")
    else:
        print(f"Ordem decrescente: {nota3}, {nota2}, {nota3}")
        input("\n Pressione qualquer tecla...")