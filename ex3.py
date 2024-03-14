n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1

if n3 > n2 and n3 > n1:
    maior = n3
    if n2 > n1:
        menor = n1
    else:
        menor = n2

print(f"O maior número é {maior}, e o menor é {menor}")