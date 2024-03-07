count = cont1 = barato = preco1 = 0
produto = ''
contbarato = ''
while True:
    print('='*25,'LOJA DO ZADIK','='*25)
    produto = str(input('nome do produto: ')).strip().lower()
    preco = float(input('digite o preço do produto: R$'))
    preco1 += preco #valor total
    if preco >=1000: #maior que 1000 reaus
        count += 1
        cont1 += 1       
    if cont1 == 1:
        barato = preco
        cont1 += 1
    if preco < barato:
        contbarato = produto
    barato = preco
    continuar = ' '
    while continuar not in 'SN': #quer ter uma
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''
        valor gasto em reais R${preco1:.2f}
        quantidade produtos acima de 1000: [{count}]
        nome do produto mais barato é {contbarato}
''')
print('='*25,'PROGRAMA ENCERRADO','='*25)


