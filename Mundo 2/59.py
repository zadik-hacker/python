#desafio 059
n1 = int(input('\033[1;35mDigite o \033[1;32m1º\033[m \033[1;35mvalor:\033[m '))
n2 = int(input('\033[1;35mDigite o \033[1;32m2º\033[m \033[1;35mvalor:\033[m '))
lista = [1,2,3,4,5]
o = 0
sair = 5
while sair != o:
    
    print('\033[1;35mESCOLHA A OPÇÃO ABAIXO\n\033[1;32m[1]\033[m somar\n\033[1;32m[2]\033[m multiplicar\n\033[1;32m[3]\033[m maior\n\033[1;32m[4]\033[m novos números\n\033[1;32m[5]\033[m sair do programa\033[m')
    o = int(input('\033[1;35mOpção aqui ==>\033[m '))
    if o == 1:
        print(f'\033[1;35mA SOMA DOS VALORES \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é = \033[1;32m{n1+n2}\033[m')
    if o == 2:
        print(f'\033[1;35mA MULTIPLICAÇÃO DOS VALORES \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é = \033[1;32m{n1*n2}\033[m')
    if o == 3:
        if n1 > n2:
         print(f'\033[1;35mO MAIOR ENTRE \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é \033[1;32m{n1}\033[m')
        elif n2 > n1:
           print(f'\033[1;35mO MAIOR ENTRE \033[1;32m{n1}\033[m e \033[1;32m{n2}\033[m é \033[1;32m{n2}\033[m')
        else:
           print(f'\033[1;35mO VALOR DOS NUMEROS E IGUAL\033[m')
    if o == 4:
       print('\033[1;35mCOLOQUE OS NOVOS NUMEROS ABAIXO\033[m')
       n1 = int(input('\033[1;35mDigite o \033[1;32m1º\033[m \033[1;35mvalor:\033[m '))
       n2 = int(input('\033[1;35mDigite o \033[1;32m2º\033[m \033[1;35mvalor:\033[m '))
    if o == 5:
       print(f'\033[1;35mVOCE ESTA SAINDO DA APLICAÇÃO\033[m')
    if o not in lista:
        print('\033[1;35mOPÇÃO INVALIDADA, TENTE NOVAMENTE\033[m')
print('\033[1;35mMUITO OBRIGADO POR TER USADO ESSA APLICAÇÃO\033[m')
   

        




