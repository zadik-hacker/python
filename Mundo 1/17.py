#desafio 017
import math
cateto = int(input('Digite o comprimento do Cateto oposto: '))
cateto2 = int(input('Digite o comprimento do Cateto Adjacente: '))
hipotenusa = math.sqrt(math.pow(cateto, 2) + math.pow(cateto2, 2))
print(f'O calculo da Hipotenusa é: {math.trunc(hipotenusa)}')
