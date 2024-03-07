#desafio 031
v = float(input('Digite a distância da viagem em quilômetros: '))
if v <= 200:
    v2 = v * 0.50
    print(f'O valor a ser cobrado pela viagem é R${v2:.2f}')
else:
    v3 = v * 0.45 
    print(f'O valor a ser cobrado pela viagem longa é R${v3:.2f}')
