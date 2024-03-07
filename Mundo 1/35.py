#desafio 035
r1 = float(input('Digite uma reta: '))
r2 = float(input('Digite outra reta: '))
r3 = float(input('Digite outra reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('AS RETAS FORMAR UM TRIANGULO')
else:
    print('NAO FORMA UM TRIANGULO')


    ### nao fiz(mas resolvido)