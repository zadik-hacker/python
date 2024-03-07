#desafio 038
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'O primeiro valor \033[32m{n1}\033[m é maior')
elif n2 > n1:
    print(f'O segundo valor \033[32m{n2}\033[m é maior')
elif n1 == n2:
    print('\033[31mO valor são iguais, logo não tem um valor maior\033[m')
