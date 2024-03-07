#desafio 49
valor = int(input('Digite um número: '))
print(f'{'\033[36m TABUADA DO ZADIK\033[m ':=^30}')
print('\033[34m=\033[m'*20)
for c in range(1, 11):
    print(f'\033[32m{valor:^5} x {c:^5} = {valor*c:^5}\033[m')
print('\033[34m=\033[m'*20)