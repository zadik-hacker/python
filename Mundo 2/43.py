#desafio 043
p = float(input('Digite seu peso (Kg): '))
a = float(input('Digite sua altura (m): '))
c = p/(a**2)
if c <= 18.5:
    print('\033[36mAbaixo do peso\033[m', end=' |')
elif c >=18.5 and c <=25:
    print('\033[36mPeso ideal\033[m', end=' |')
elif c >=25 and c <= 30:
    print('\033[36mSobrepeso\033[m', end=' |')
elif c >=30 and c <= 40:
    print('\033[36mObesidade\033[m', end=' |')
elif c > 40:
    print('\033[36mObesidade mórbida\033[m', end=' |')
print(f'Seu \033[32mIMC\033[m é: \033[34m{c:.1f}\033[m')
