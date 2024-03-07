#desafio 004
trabalho = (input('informação: '))
print(f'tipo primitivo da questão{type(trabalho)}')
print(f'É um numero? {trabalho.isnumeric()}')
print(f'É alfabético? {trabalho.isalpha()}')
print(f'Contém espaços? {trabalho.isspace()}')
print(f'É alfanumerico? {trabalho.isalnum()}')
print(f'Está em maiúsculas? {trabalho.isupper()}')
print(f'Está em Minúsculas? {trabalho.islower()}')
print(f'Está Capitalizada? {trabalho.istitle()}')

#isalnum – Verifique se todos os caracteres no texto são alfanuméricos
#isalpha – Verifique se todos os caracteres no texto são letras
#isascii – Verifique se a sequência é composta por todos os caracteres ASCII ou se a sequência estiver vazia também retornara true
#isdecimal – Verifique se todos os caracteres no objeto unicode são decimais
#isdigit – Verifique se todos os caracteres no texto são dígitos
#isidentifier – Verifique se a sequência é um identificador válido :: O método isidentifier () retornará True se a string for um identificador válido, caso contrário, False. Uma sequência é considerada um identificador válido se contiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.
#islower – Verifique se todos os caracteres do texto estão em minúsculas
#isnumeric – Verifique se todos os caracteres no texto são numéricos
#isprintable – Verifique se todos os caracteres no texto são imprimíveis
#isspace – Verifique se todos os caracteres no texto são espaços em branco
#istitle – Verifique se cada palavra começa com uma letra maiúscula
#isupper – Verifique se todos os caracteres do texto estão em maiúsculas