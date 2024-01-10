#soma_digito
n = int(input("Digite um número inteiro: "))

soma_digitos = 0

while n > 0:
    # Adicione o dígito atual à soma
    soma_digitos += n % 10
    # Remova o dígito atual do número
    n //= 10

# Imprima a soma dos dígitos
print(soma_digitos)