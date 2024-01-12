#troca a posição dos números 
def inverte_py(lista):
    return list(reversed(lista))

# Lista para armazenar os números
numeros = []

# Solicita ao usuário para digitar números até que 0 seja inserido
while True:
    num = int(input("Digite um número: "))
    
    # Se o número digitado for 0, encerra o loop
    if num == 0:
        break
    
    # Adiciona o número à lista
    numeros.append(num)

# Usa a função inverte_py para inverter a ordem dos números na lista
numeros_invertidos = inverte_py(numeros)

# Imprime os números invertidos
for num in numeros_invertidos:
    print(num)

    