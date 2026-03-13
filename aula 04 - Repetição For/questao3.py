##Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso. 
contador = 0
x = int (input("Digite o valor de x: "))
for lia in range(1,x+1):
    if lia % 2 != 0:
        print(lia)

