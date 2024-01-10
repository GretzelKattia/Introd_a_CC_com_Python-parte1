n = int(input("Digite  valor de n: "))
contagem = 0
numero_atual = 1
while contagem < n:
    if numero_atual % 2 != 0:
        print(numero_atual)
        contagem += 1
    numero_atual += 1
