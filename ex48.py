def maior(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = maior(num1, num2)

print("O maior número é:", resultado)