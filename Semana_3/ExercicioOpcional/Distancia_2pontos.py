import math
x1=int(input("Digite a coordenada x: "))
y1=int(input("Digite a coordenada y: "))
x2=int(input("Digite a coordenada x: "))
y2=int(input("Digite a coordenada y: "))

Dis= math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if (Dis>=10):
    print("longe")
else:
    print("perto")

        
