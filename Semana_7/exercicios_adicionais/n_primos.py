def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def n_primos(n):
    primos = []
    for num in range(2, n + 1):
        if eh_primo(num):
            primos.append(num)
    return len(primos)

# Exemplo de uso
numero_teste = int(input("Digite um número: "))
resultados = n_primos(numero_teste)
print(f"Números primos entre 2 e {numero_teste}: {resultados}")