#desafio 051
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1, 11):
    pt = t + (c-1) * r
    if c == 10:
        print(f'\033[32m{pt}\033[m')
    else:
        print(f'\033[32m{pt}\033[m', end='\033[34m==>\033[m')