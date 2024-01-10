#Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(a,b):

    if a>b:
        return a
    else:
        return b
    
num1=float(input("Digiite o primeiro valor: "))
num2=float(input("Digite o segundo valor: "))
val=maximo(num1, num2)
print(val)