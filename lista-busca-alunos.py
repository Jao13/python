lista = []

while True:
    nome = input("Digite um nome(ou 'sair'): ")
    if nome == "sair":
        break
    else:
        lista.append(nome)

busca = input("digite um termo para procurar: ")

i = 0
contador = 0

for i in range(len(lista)):
    if busca in lista[i]:
        print(f"{lista[i]}")