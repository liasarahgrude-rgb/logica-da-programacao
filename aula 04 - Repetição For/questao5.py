##Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida. Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir apenas NULO. 
num = int(input("Quantos números você vai digitar? "))
for paridade in range(num):
    valor = int(input("Digite um valor: "))
    if valor > 0:
        if valor % 2 == 0:
            print(f"Este valor é positivo e par!")
        elif valor % 2 != 0:
            print(f"Este valor é positivo e impar!")
    elif valor < 0:
        if valor % 2 == 0:
            print(f"Este valor é negativo e par!")
        elif valor % 2 != 0:
            print(f"Este valor é negativo e impar!")
    else:
        print(f"Esse valor é nulo!")