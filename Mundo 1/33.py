#desafio 033
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
if n1 > n2 > n3:
    print(f'{n1:.0f} é maior {n3:.0f} menor')
else:
 if n3 > n2 > n1:
    print(f'{n3} é maior {n1:.0f} menor')
 else:
  if n1 > n3 > n2:
    print(f'{n1:.0f} é maior {n2:.0f} menor')
  else:
    if n3 > n1 > n2:
      print(f'{n3} é maior {n2:.0f} menor')
    else:
      if n2 > n3 > n1:
        print(f'{n2:.0f} é maior {n1:.0f} menor')
      else:
       if n2 > n1 > n3:
        print(f'{n2:.0f} é maior {n3:.0f} menor')

      
    


    


