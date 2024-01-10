#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

#SAIDA
###Digite um número inteiro: 13
###primo

# Entrada do usuário
num=int(input("Digite um número inteiro: "))


# Inicializar variáveis
divisor = 2
primo = True

# Verificar se é primo usando while e if-else
while divisor < num:
    if num % divisor == 0:
        primo = False
        break
    divisor += 1

# Imprimir o resultado
if primo and num > 1:
    print("Primo")
else:
    print("Não primo")
