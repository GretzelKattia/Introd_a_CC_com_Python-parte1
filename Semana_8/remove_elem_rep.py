def remove_repetidos (lista):
    #remove elementos repetidos
    lista_sem_repetição = list(set(lista))

    #ordena a lista resultante
    lista_sem_repetição.sort()
    return lista_sem_repetição

#EXEMPLO DE LISTA
numero=[3,6,2,8,3,9,3,8,5,0,1,9,3,7,3,6]
resultado = remove_repetidos(numero)

print(f"lista original {numero}")
print(f"lista sem repetição de números {resultado}")
