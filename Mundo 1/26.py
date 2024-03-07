#desafio 026
frase = str(input('Digite a frase: ')).strip().upper()
f1 = frase.count('A')
f2 = frase.find('A')+1
f3 = frase.rfind('A')+1
print(f'NUMERO DE VEZES QUE APARECEU A LETRA A: {f1}\nNUMERO DA PRIMEIRA POSIÇÃO DA LETRA A: {f2}\nNUMERO DA ULTIMA POSIÇÃO DA LETRA A: {f3}')
