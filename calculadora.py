import os
import math

opcao = 0
while opcao != 7:
    os.system("cls")
    print("------ CALCULADORA ------")
    print("Escolha uma opção:")
    print("[ 1 ] ADIÇÃO")
    print("[ 2 ] SUBTRAÇÃO")
    print("[ 3 ] DIVISÃO")
    print("[ 4 ] MULTIPLICAÇÃO")
    print("[ 5 ] RAIZ-QUADRADA")
    print("[ 6 ] POTENCIA")
    print("[ 7 ] SAIR")

    opcao = int(input("Escolha uma opção: "))

    if opcao >= 1 and opcao <= 4:
       x = int(input("Digite um numero: "))
       y = int(input("Digite outro numero: "))

    if opcao == 1:
       print(f"O resultado é: {x + y}")
       input("\nPressione alguma tecla...")
   
    if opcao == 2:
       print(f"O resultado é: {x - y}")
       input("\nPressione alguma tecla...")

    if opcao == 3:
       print(f"O resultado é: {x / y}")
       input("\nPressione alguma tecla...")

    if opcao == 4:
       print(f"O resultado é: {x * y}")
       input("\nPressione alguma tecla...")

    if opcao == 5:
       raiz_quadrada = int(input("Digite um numero: ")) 
       print(f"O resultado da raiz-quadrada é: {math.sqrt(raiz_quadrada)}")
       input("\nPressione alguma tecla...")

    if opcao == 6:
       potencia = int(input("Digite outro numero: "))
       elevado = int(input("Digite um numero que vai ser elevado: "))
       print(f"O resulrado da potenciação é: {potencia ** elevado}")
       input("\nPressione alguma tecla...")

    if opcao == 7:
       print("Até a proxima")
