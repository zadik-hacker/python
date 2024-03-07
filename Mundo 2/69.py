#desafio 069
idade18 = idadeM = idadeF = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o gênero [M/F]: ')).strip().upper()[0]
    if (sexo == 'F' or 'M') and idade < 18: #menores de 18
        idade18 += 1
    elif sexo == 'M' and idade > 18:
        idadeM += 1
    elif sexo == 'F' and idade < 20:
        idadeF += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'''
TOTAL DE PESSOAS MENORES DE 18 ANOS: {idade18}
TOTAL DE MULHERES COM MENOS DE 20 ANOS: {idadeF}
TOTAL DE HOMENS MAIORES DE 18 ANOS: {idadeM}
''')


    
