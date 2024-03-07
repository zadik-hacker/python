#desafio 053
for c in range(0, 100000):
    frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
    inverso = frase[::-1]#usa o -1 negativo para ir para o final da frase e os dois ponto para inverter
    if frase == inverso:
        print(f'\033[32mA frase ==> \033[35m{frase}\033[m \033[32mcontém um palíndromo ==>\033[m \033[35m{inverso}\033[m')#bloco true
    else:
        print(f'\033[31mA frase ==> \033[35m{frase}\033[m \033[31mnão contém palíndromo\033[m')#bloco false
        