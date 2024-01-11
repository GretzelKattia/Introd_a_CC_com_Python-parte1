
largura=int(input("Digite a largura: "))
altura=int(input("Digite a altura: "))

linha=0

while linha<altura:
    coluna=0
    while coluna < largura:
        print("#", end="")
        coluna += 1
    print()  # Pula para a próxima linha após imprimir uma linha completa de '#'s
    linha += 1
