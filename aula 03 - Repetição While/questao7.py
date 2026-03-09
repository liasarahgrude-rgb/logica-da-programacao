##Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a mensagem "IMPOSSIVEL CALCULAR". 
soma = 0
quantidade = 0
idade = int(input("Digite a idade: "))
if idade <= 0:
    print("IMPOSSIVEL CALCULAR")
else:
    while idade > 0:
        soma = soma + idade          
        quantidade = quantidade + 1     
        
        idade = int(input("Digite a próxima idade: "))

    media = soma / quantidade
    print(f"Média: {media:.2f}")