#desafio 034
salario = float(input('Digite o salario do funcionario: '))
if salario >= 1250:
   s2 = 0.10*salario
   s3 = s2+salario
   print(f'o aumento do salario foi de 10% dando R${s3:.2f}')
else:
   if salario < 1250:
      s2 = 0.15*salario
      s3 = s2+salario
      print(f'o aumento do salario foi de 15% dando R${s3:.2f}')