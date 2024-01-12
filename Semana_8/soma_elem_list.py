def soma_elementos (lista):
    #remove elementos repetidos
    soma=0
    for elemento in lista:
        soma += elemento


    return soma

#EXEMPLO DE LISTA
numero=[3,6,2,8,3,9]
resultado = soma_elementos(numero)

print(f"a soma total dos elementos da lista: {resultado}")
