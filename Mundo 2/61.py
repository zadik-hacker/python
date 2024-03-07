#desafio 061
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
limit = 1
while limit != 11:
    pa = t + (limit - 1)*r
    limit +=1
    print(f'\033[32m{pa}\033[m', end='\033[34m==>\033[m') 
print(f'\033[1;36mFIM\033[m')


 #   c=1
#while c !=10:
 #    print(c)
  #   c+=1
#print('Acabou')
    

