#desafio 067
import os
def apagar_terminal():
    os.system('cls')
t = v = 0
while True:
    t = int(input('Qual valor da tabuada voce quer ver? '))
    if t < 0:
        apagar_terminal()
        break
    v = t
    print('==='*5)
    for c in range(1,11):
        print(f'{v} x  {c:^2} = {t*c:^5}')
    print('==='*5)
print('TABUADA NAO ACEITA POR SER NEGATIVA, ENCERRANDO...')