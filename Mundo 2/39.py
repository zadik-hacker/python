#desafio 039
from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))
jovem = date.today().year - nascimento 
a = date.today().year
if a < nascimento:
    print('voce ainda nem nasceu caralho!!')
else:
    if jovem > 17 and jovem <=22: #pode ainda
     n1 = abs(jovem - 22) # o abs() serve para retornar o numero absoluto, tirando negativo na conta, ele ja vem no python
     print(f'voce ainda pode ser alistar ao serviço militar por {n1} ano(s) ainda')
    elif jovem == 17: #deve se alistar obrigatoriamente
     print('voce deve se alistar ao serviço militar imediatamente!')
    elif jovem > 22: #passou do tempo
     n2 = abs(jovem - 22)
     print(f'voce ja passou do tempo de alistamento á {n2} ano(s) atras')
    elif jovem < 17: #caso não tenha
     n3 = abs(jovem - 17)
     print(f'voce ainda não pode se alistar ao serviço militar falta {n3} ano(s)')



