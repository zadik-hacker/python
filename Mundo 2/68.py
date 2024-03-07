#desafio 068
from random import randint
cont = 0
while True:
    v = int(input('Digite um valor: '))
    digito = str(input('Par ou Ímpar [P/I]: ')).upper().strip()
    valorsomado = randint(1, 10) + v
    if digito != 'P' and digito != 'I':
        print('tente novamente, use apenas as caracteres [P/I]')   
    elif (valorsomado % 2) == 0 and digito == 'P':
        print(f'O GANHADOR FOI VOCÊ, O VALOR FOI {valorsomado} SENDO PAR\n')
        cont += 1
    elif (valorsomado % 2) == 1 and digito == 'I':
        print(f'O GANHADOR FOI VOCÊ, O VALOR FOI {valorsomado} SENDO IMPAR\n')
        cont += 1
    elif (valorsomado % 2) == 0 and digito != 'P':
        print(f'O GANHADOR FOI O BOT, O VALOR FOI {valorsomado} SENDO PAR\nSUA SEQUENCIA DE VITORIA FOI {cont}')
        break
    elif (valorsomado % 2) == 1 and digito != 'I':
        print(f'O GANHADOR FOI O BOT, O VALOR FOI {valorsomado} SENDO IMPAR\nSUA SEQUENCIA DE VITORIA FOI {cont}')
        break
print('Obrigado por ter usado minha aplicação.')
