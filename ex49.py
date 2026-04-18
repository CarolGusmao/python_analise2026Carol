def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b != 0:
        return a / b
    else:
        print("Valor inválido (divisão por zero)")
        return None


escolha = ""

while escolha != "0":
    escolha = input("\nDigite uma opção: 1-somar, 2-subtrair, 3-multiplicar, 4-dividir, 0-sair: ")

    if escolha == "0":
        print("Operação terminada")
        break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == "1":
        x = somar(num1, num2)

    elif escolha == "2":
        x = subtrair(num1, num2)

    elif escolha == "3":
        x = multi(num1, num2)

    elif escolha == "4":
        x = divi(num1, num2)

    else:
        print("Opção inválida")
        continue

    print(f"O resultado da operação é: {x}")
