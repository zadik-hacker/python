#desafio 012
preço = float(input('Preço do produto: R$'))
desconto = preço/100
desconto2 = preço-(desconto*5)
print(f'O Novo valor do produto é de: R${desconto2}')
