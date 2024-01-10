# Entrada do usuário
numero = input("Digite um número inteiro: ")

# Inicializar a variável para verificar se há dígitos adjacentes iguais
tem_adjacente_igual = False

# Verificar se há dígitos adjacentes iguais usando while e if-else
indice = 0
while indice < len(numero) - 1:
    if numero[indice] == numero[indice + 1]:
        tem_adjacente_igual = True
        break
    indice += 1

# Imprimir o resultado
if tem_adjacente_igual:
    print("sim")
else:
    print("não")
