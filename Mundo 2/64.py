#desafio 064
n = soma = count = 0
n = int(input('Digite um número inteiro [999 para parar]: '))
while n != 999:   
    soma += n
    count +=1
    n = int(input('Digite um número inteiro[999 para parar]: '))
print(f'A quantidade de números digitados foi {count}, é a soma entre eles é {soma}')
