#desafio 024
nome = str(input('Digite o nome de uma cidade: ')).strip().upper().split()
cidade = ('SANTO' in nome[:5])
print(f'True para a cidade que começa com SANTO, e False para a cidade que não começa com SANTO\nA Cidade é: {cidade}')
