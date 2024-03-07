#desafio 060
from math import factorial
digito=''
n= 0
while digito != 'N':
        n= int(input('Digite um número: '))
        f = factorial(n)
        f1 = factorial(f)
        print(f'Factorial de {n} = {f}')
        digito= str(input('Que continuar digite ==> [S/N] ')).upper().strip()
print(f'Obrigado por ter usado minha aplicação')
    