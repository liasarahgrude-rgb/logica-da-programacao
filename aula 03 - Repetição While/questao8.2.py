##Enunciado igual da questão 8 com a resolução por while 
senha_correta = 2002
senha = int(input ("Digite a senha correta: "))
while senha != senha_correta:
    print("Senha Invalida! Tente novamente!")
    senha = int(input ("Digite a senha correta: "))
print("Acesso permitido!")