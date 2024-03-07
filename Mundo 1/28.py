#desafio 028
from random import randint
acerto = randint(0, 5)
tente = int(input('Digite o numero de 0 a 5: '))
if tente > 5:
    print('escreva como foi descrito!!! ou voce vai sempre perder')
if acerto == tente:
    print(f'voce me venceu o numero era {acerto}')
else:
    print(f'voce perdeu o numero era {acerto}')