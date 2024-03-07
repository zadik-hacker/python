#desafio 027
nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.split()[0]
n2 = nome.split()[-1] #indice -1 vai pro ultimo item da lista
print(f'primeiro: {n1}\nsegundo: {n2}')
