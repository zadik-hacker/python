#desafio 042
r1 = float(input('Coloque o primeiro segmento: '))
r2 = float(input('Coloque o segundo segmento: '))
r3 = float(input('Coloque o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mUM TRIANGULO FOI FORMADO\033[m', end='  ')
    if r1 == r2 ==r3: 
        print('TODOS OS LADOS SÃO IGUAIS LOGO SENDO EQUILÁTERO')
    elif r1 != r2 and r1 != r3 and r2 != r3 and r3 !=r2:
        print('TODOS OS LADOS SÃO DIFERENTES SENDO ESCALENO')
    else: 
        print('DOIS LADOS SÃO IGUAIS SENDO ISÓSCELES')
else:
    print('\033[34mNAO FORMA NENHUM TRIANGULO\033[m')

'''r1 = float(input('Digite uma reta: '))
r2 = float(input('Digite outra reta: '))
r3 = float(input('Digite outra reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('AS RETAS FORMAR UM TRIANGULO', end=' ')
    if r1 ==r2 ==r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('ISÓsceles')
else:
    print('NAO FORMA UM TRIANGULO')'''