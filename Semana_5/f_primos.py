#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao 
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def maior_primo(numero):
    while numero >= 2:
        if eh_primo(numero):
            return numero
        numero -= 1


#Exemplo de execução
numero_teste = int(input("Digite um número: "))
resultado = maior_primo(numero_teste)
print(resultado)
