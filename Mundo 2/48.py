#desafio 048
soma = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 2) !=0 and (c % 3) ==0:
     cont =+1
     soma +=c 
print(f'\033[32mESSE SÃO TODOS OS {cont} NUMEROS IMPARES, MÚLTIPLOS DE 3 ENCONTRADOS NO INTERVALO DE 1 ATE 500 é a soma deles da => {soma}\033[m')