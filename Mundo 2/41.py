#desafio 041
from datetime import date
nascimento = int(input('Digite sua data de nascimento: '))
if nascimento > date.today().year:
    print('\033[32mAno de nascimento invalido, TENTE NOVAMENTE!!\033[m')
else:
    ano = abs(date.today().year - nascimento)
    if ano >=4 and ano <=9: #ate 9 anos
     print('SUA CATEGORIA E \033[32mMIRIM\033[m DENTRO DA NATAÇÃO') 
    elif ano >=10 and ano <=14: #ate 14 anos
        print('SUA CATEGORIA E \033[32mINFANTIL\033[m DENTRO DA NATAÇÃO')
    elif ano >=15 and ano <=19: #ate 19 anos
        print('SUA CATEGORIA E \033[32mJUNIOR\033[m DENTRO DA NATAÇÃO')
    elif ano ==20: #ate 20 anos
      print('SUA CATEGORIA E \033[32mSÊNIOR\033[m DENTRO DA NATAÇÃO')
    elif ano > 20: #maior que 20 anos
        print('SUA CATEGORIA E \033[35mMASTER\033[m DENTRO DA NATAÇÃO')
    else:
        print('\033[31mVOCE NÃO TEM IDADE SUFICIENTE PARA PARTICIPAR DA NATAÇÃO\033[m')