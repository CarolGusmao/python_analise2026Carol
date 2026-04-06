valor= float(input("Olá! :) Digite o valor do produto :"))
if valor >= 500 :
        desconto= (valor *20) / 100
        p= valor - desconto
        print(f"O desconto elegível para este item é {desconto}. Valor final é {p}")
elif valor <= 99:
        desconto= (valor * 5) /100
        p= valor - desconto
        print(f"O desconto elegível para este item é {desconto}. Valor final é {p}")
else:
        desconto= (valor * 15) /100
        p= valor - desconto
        print(f"O desconto elegível para este item é {desconto}. Valor final é {p}")
        