c50 = c20 = c10 = c1 = 0
valor = int(input('digite o valor a ser sacado: R$'))
while True:
    if valor >=50:
        valor -= 50
        c50 += 1
    elif valor >= 20:
        valor -= 20
        c20 += 1
    elif valor >= 10:
        valor -= 10
        c10 += 1
    elif valor >= 1:
        valor -= 1
        c1 += 1
    if valor == 0:
        break
print(f'''
      QUANTIDADE DE CEDULAS
      R$50 [{c50}]
      R$20 [{c20}]
      R$10 [{c10}]
      R$1  [{c1}]
''')
      
