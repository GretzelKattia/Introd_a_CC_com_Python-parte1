def eh_hipotenusa(h):
    for i in range(1, h):
        for j in range(1, h):
            if i**2 + j**2 == h**2:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for h in range(1, n + 1):
        if eh_hipotenusa(h):
            soma += h
    return soma

n = 25  # Substitua pelo valor desejado
resultado = soma_hipotenusas(n)
print(f"A soma das hipotenusas até {n} é: {resultado}")
