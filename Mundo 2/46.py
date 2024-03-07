#desafio 046
from time import sleep
from datetime import date
from emoji import emojize
print('\033[32mQUE COMECE A CONTAGEM DO ANO NOVO\033[m')
a = date.today().year + 1
for c in range(10, 0, -1):
    print(emojize(f'{c}:firecracker:'))
    sleep(1)
print(emojize(f'\033[33mFELIZ ANO NOVO QUE {a} SEJA INCRÍVEL\033[m:confetti_ball::party_popper::fireworks:'))