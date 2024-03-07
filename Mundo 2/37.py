#desafio 037
n = int(input('digite um numero: '))
n2 = int(input('digite o valor abaixo para converter\n1- binario\n2- octal\n3- hexadecimal\ncoloque aqui: '))
b = bin(n)[2:] #numero em binario
o = oct(n)[2:] #numero em octal
h = hex(n)[1:] #numero em hexdecimal
if n2 ==1:
    print(f'o número \033[32m{n}\033[m covertido em binario é \033[32m{b}\033[m')
elif n2 ==2:
    print(f'o número \033[32m{n}\033[m convertido em octal é \033[32m{o}\033[m')
elif n2 ==3:
    print(f'o número \033[32m{n}\033[m convertido em hexadecimal é \033{h}\033[m')
elif n2 != 1 or 2 or 3:
    print('\033[31mvoce colocou o digito errado tente novamente!\033[m')