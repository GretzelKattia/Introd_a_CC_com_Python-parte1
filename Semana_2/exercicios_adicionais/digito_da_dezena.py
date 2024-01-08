#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:


numero = int(input("Digite um número inteiro: "))

dezena = (numero // 10) % 10
 
    
print("O dígito das dezenas é", dezena)
