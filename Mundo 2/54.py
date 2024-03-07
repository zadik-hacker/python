#desafio 054
from datetime import date
soma = 0
soma2 = 0
for c in range(0, 7):
    p = int(input('\033[35mDigite seu ano de nascimento aqui ==>\033[m '))
    data =  abs(p - date.today().year)
    if data >=21:
        soma += 1
    elif data <21:
        soma2 += 1
print(f'\033[32m{soma}\033[m pessoas atingiu a maioridade')
print(f'\033[31m{soma2}\033[m pessoas ainda não atingiu a maioridade')    
    
