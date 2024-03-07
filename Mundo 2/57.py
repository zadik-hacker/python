#desafio 057
mulher = 'F'
homem = 'M'
string_vazia =''
while string_vazia != mulher and string_vazia != homem:
    string_vazia = str(input('Digite seu sexo [M/F] ==> ')).upper().strip()[0] #para pegar a primeira letra, isto é um fatiamento
    if string_vazia != mulher and string_vazia != homem:
        print('digite apenas [M/F] , tente novamente!!')
if string_vazia =='F':
    print('voce é linda, do sexo feminino')
else:
    print('voce é bonito, do sexo masculino')

