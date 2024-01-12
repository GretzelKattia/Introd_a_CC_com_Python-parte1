#Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):
    if not lista:
        # Retorna None se a lista estiver vazia
        return None
    
    # Inicializa a variável para armazenar o maior elemento
    maior = lista[0]

    # Itera sobre a lista para encontrar o maior elemento
    for num in lista:
        if num > maior:
            maior = num

    return maior

# Exemplo de uso da função
lista_exemplo = [5, 12, 8, 3, 15, 7]
resultado = maior_elemento(lista_exemplo)

print("O maior elemento da lista é:", resultado)
