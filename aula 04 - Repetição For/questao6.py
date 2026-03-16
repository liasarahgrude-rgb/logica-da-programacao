##Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida pela soma dos pesos. 
casos = int(input("Quantos casos voce vai digitar? "))
for teste in range(casos):
    val = float(input("Digite tres numeros: "))
    peso1 = [0,1] * 2
    print(f"{peso1}") 