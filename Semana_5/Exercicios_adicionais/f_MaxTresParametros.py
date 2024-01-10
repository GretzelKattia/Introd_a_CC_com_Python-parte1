
def maximo(a,b,c):

    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    else:
        return a or b or c
    

num1=float(input("Digiite o primeiro valor: "))
num2=float(input("Digite o segundo valor: "))
num3=float(input("Digite o terceiro valor: "))

val=maximo(num1, num2, num3)
print(val)