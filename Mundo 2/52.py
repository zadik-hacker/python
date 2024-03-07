#desafio 052
divisao = 0
n = int(input('Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        divisao += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if divisao == 2:
    print(f'\nO número \033[32m{n}\033[m é um número primo, pois tem \033[32m{divisao}\033[m divisores')
else:
    print(f'\nO número \033[31m{n}\033[m não é um número primo, pois tem \033[31m{divisao}\033[m divisores')
    