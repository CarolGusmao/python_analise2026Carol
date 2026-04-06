v=input("Digite 3 valores inteiros diferentes entre si :")
n1=int(input('Digite nº1:'))
n2=int(input('Digite nº2:'))
n3=int(input("Digite nº3:"))
if n1> n2 and n1 > n3 :
    print(f'{n1} é o maior número!')
elif n2> n1 and n2 > n3:
    print(f'{n2} é o maior número!')
else:
    print(f'{n3}é o maior número')
