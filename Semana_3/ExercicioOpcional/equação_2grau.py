import math
a=int(input("Digite um número para a: "))
b=int(input("Digite um número para b: "))
c=int(input("Digite um número para c: "))


delta= (b**2)-(4*a*c)

if (delta<0):
    print("esta equação não possui raízes reais")
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    if(delta==0):
        print("a raiz dupla desta equação é", x1)
    else:
        x2=(-b-math.sqrt(delta))/(2*a)
        if(x1<x2):
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)
