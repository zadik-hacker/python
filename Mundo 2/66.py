#desafio 066
'''n = s = 0
while True:
    n = int(input('digite um numero: '))
    if n ==999:
        break
    s +=n
print(f'{s}')'''

n = s = 0
count = 0
while True:
    n = int(input(f'digite o um numero:'))
    if n ==999:
        break
    count +=1
    s += n
print(f'A Soma dos valores é {s} e foram digitados {count} números')
