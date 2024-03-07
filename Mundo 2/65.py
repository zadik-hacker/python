#desafio 065
soma = count = media = maior = menor= 0
digito = 'S'
while digito in 'Ss':
    n = int(input('Digite um número: '))     
    soma += n
    count += 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    digito = str(input('Quer continuar colocando números? DIGITE [S/N]')).upper().strip()[0]
media += soma / count
print(f'Voce digitou {count} numeros e a média foi {media}', end=' ')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('OBRIGADO POR TER USADO MINHA APLICAÇÃO')
