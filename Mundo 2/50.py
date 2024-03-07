#desafio 050
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if (n % 2) ==0:
        soma +=c
        cont += 1
print(f'A soma de \033[32m{cont}\033[m números pares é \033[32m{soma}\033[m')
