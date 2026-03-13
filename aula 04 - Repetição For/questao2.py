##Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números impares entre eles.
contador = 0
x = int (input("Digite o valor de x: "))
y = int (input("Digite o valor de y: "))
for lia in range(x,y):
    if lia % 2 != 0:
        contador += lia
print(f"A soma dos números ímpares entre {x} e {y} é: {contador}")


    