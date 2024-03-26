lista = []

while True:
    nome = input("Digite um nome (ou 'sair'): ")
    if nome == "sair":
        break
    else:
        lista.append(nome)

busca = input("Deseja buscar um nome?: ")

if busca in lista:
    print(f"{busca} foi encontrado!")
else:
    print(f"{busca} não foi encotrado!")