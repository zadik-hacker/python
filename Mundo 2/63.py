#desafio 063
n = int(input('Digite um numero inteiro: '))
a, b = 0,1
while a < n:
    a, b = b, a +b
    print(a, end='=> ')
print('FIM')


