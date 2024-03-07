#desafio 058
from random import randint
from time import sleep
numero = randint(0, 10)
Valor=0
digito=''
while numero != digito:
    digito = int(input('\033[35mdigite um numero de 0 a 10 ===>\033[m' ))
    if digito != numero:
        print('voce errou tente novamente!!', end=' ')
        if digito > numero:
            print(f'MENOS QUE {digito}...')
        elif digito < numero:
            print(f'MAIS QUE {digito}...')
        Valor += 1
print('\033[32mPROCESSANDO...\033[m')
sleep(3)
print(f'Voce acertou o número era \033[32m{numero}\033[m, foi \033[32m{Valor}\033[m Tentativas')

