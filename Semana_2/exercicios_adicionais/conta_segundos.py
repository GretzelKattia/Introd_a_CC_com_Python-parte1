#Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
#faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
#A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato!
#Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro
segundo_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundo_str)

dias = total_segs //86400
segs_restantes_prim = total_segs % 86400
horas = segs_restantes_prim // 3600
segs_restantes_seg = segs_restantes_prim % 3600
minutos = segs_restantes_seg // 60
segs_restantes_final = segs_restantes_seg % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
