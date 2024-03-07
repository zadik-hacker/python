#desafio 044
print(f'{'\033[36m LOJAS DO ZADIK\033[m ':=^40}')
p = float(input('Preço do produto: R$'))
m = str(input('\n\033[32mdinheiro/cheque ou pix 10% de desconto\ncartão 5% de desconto\n2x parcelas no cartão sem juros preço normal\n3x parcelas ou mais no cartão 20% de juros\n\033[mForma de pagamento: ')).lower().strip()
if m =='dinheiro' or m=='cheque' or m=='pix':
    print(f'O seu produto teve um desconto de 10% é foi para R${p-(p*10)/100:.2f}')
elif m =='cartao' or m =='cartão':
    print('digite 1- para não parcelar e ganhar um desconto de 5%\ndigite 2- para parcelar em 2x no cartão sem desconto\ndigite 3- para parcelar em 3x ou mais com 20% de juros')
    p1 = int(input('digite aqui: '))
    if p1 ==1: 
        print(f'O seu produto teve um desconto de 5% é foi para R${p-(p*5)/100:.2f}')
    elif p1 ==2:
        print(f'O seu produto teve nenhum desconto é ficou com 2x parcelas de R${p/2:.2f} para pagar o valor R${p:.2f}')
    elif p1 ==3:
        p2 = int(input('digite o número de parcelas: '))
        if p2 >=3:
         juros = 0.20
         v = p+(p*juros)
         p4 = v/p2
         print(f'O seu produto teve 20% de juros com um total de {p2}x parcelas de R${p4:.2f} para pagar o valor de R${v:.2f}')
        else:
            print(f'O seu produto teve nenhum desconto é ficou com 2x parcelas de R${p/2:.2f} para pagar o valor R${p:.2f}')
    else:
        print('digitou um número fora da lista tente novamente!!!')
else:
    print('digitou o nome errado da forma de pagamento tente novamente!!!')
        
    
    
