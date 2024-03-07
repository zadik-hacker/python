#desafio 032
from datetime import date
a = int(input('digite o ano, caso queira o ano anual coloque 0: '))
if a ==0:
    a = date.today().year
if (a % 4 == 0 and a % 100 != 0) or a % 400 ==0:      
    print(f'sim, o ano {a} é bissexto')
else:
    print(f'não, o ano {a} não é bissexto')