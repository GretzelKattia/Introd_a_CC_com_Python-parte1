#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.


def vogal(caractere):
    vogais = 'aeiouAEIOU'
    return caractere.lower() in vogais

# Exemplos de execução
vol=input("Digite uma vogal: ")
print(vogal(vol)) 

