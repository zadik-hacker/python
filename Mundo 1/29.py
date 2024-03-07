#desafio 029
carro = int(input('Digite a velocidade do carro: '))
multa = (carro-80)*7.0
if carro > 80:
    print(f'voce foi multado em R${multa:.2f}')
else:
    print('voce não foi multado')
