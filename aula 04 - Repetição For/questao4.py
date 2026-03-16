##Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo
valor = int(input("Quantos números você vai digitar? "))
dentro = 0
fora = 0
for num in range(valor):
    usuario = int(input("Digite um número: "))
    if 10 <= usuario <= 20:
        dentro += 1
    else:
        fora += 1
print(f"{dentro} dentro do intervalo [10,20]")
print(f"{fora} fora do intervalo [10,20]")