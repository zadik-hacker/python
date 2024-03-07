#desafio 036
casa = float(input('Valor da casa: R$')) #casa valor
salario = float(input('Valor da renda do cliente: R$')) #salario 
ano = int(input('Quantos anos o cliente ira pagar: ')) #anos 
p = casa/(ano*12) #presteção mensal
m = salario*30/100 #execeder os 30%
if p <=m: 
    print(f'\033[32ma casa foi comprada com sucesso em {ano} anos em prestaçoes mensais de R${p:.2f}\033[m')
else:
    print(f'\033[31ma casa não pode ser comprada o valor execede os 30% da prestação mensal\033[m')
