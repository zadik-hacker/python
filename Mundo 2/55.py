#deseafio 055
soma = 0
soma2 = 0
for c in range(1, 6):
    peso = float(input(f'Digite o \033[32m{c}º\033[m peso ==> '))
    if c ==1:
        soma = peso
        soma2 = peso
    else:
        if peso> soma:
            soma = peso
        if peso < soma2:
            soma2 = peso
print(f'O \033[34mMaior\033[m Peso lido Foi \033[32m{soma}\033[mKg')
print(f'O \033[31mMenor\033[m Peso lido Foi \033[32m{soma2}\033[mKg')