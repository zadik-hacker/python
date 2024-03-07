#desafio 045
from random import choice
from emoji import emojize
from time import sleep
jv = ['pedra','papel', 'tesoura'] #lista de palavras permitida em uma lista
j = str(input(emojize('Escreva sua opção:\npedra:raised_fist:\npapel:raised_back_of_hand:\ntesoura:victory_hand:\ndigite aqui ==> '))).strip().lower() #voce
b = choice(['papel','pedra','tesoura']) #bot
print('JOKEEEENPO')
sleep(2)
v = '\033[31m' #inimigo/vermelho
a = '\033[36m' #azul
r = '\033[34m' #roxo
f =  '\033[m' #a var f e de final
if j not in jv:
    print('\033[31mEscolha não permitida, use apenas pedra - papel ou tesoura!!\033[m')
else:
    if j=='pedra' and b=='papel':
        print('='*20)
        print(emojize(f'{a}jogador:{f} pedra:raised_fist:\n{v}Bot:{f} papel:raised_back_of_hand:\nO {v}Bot{f} ganhou!'))#bot
        print('='*20)
    elif b=='pedra' and j=='papel':
        print('='*20)
        print(emojize(f'{a}jogador:{f} papel:raised_back_of_hand:\n{v}Bot:{f} pedra:raised_fist:\nO {a}Jogador{f} ganhou!'))#jogador
        print('='*20)
    elif j=='tesoura' and b=='papel':
        print('='*20)
        print(emojize(f'{a}jogador:{f} tesoura:victory_hand:\n{v}Bot:{f} papel:raised_back_of_hand:\nO {a}Jogador{f} ganhou!'))#jogador
        print('='*20)
    elif b=='tesoura' and j=='pedra':
        print('='*20)
        print(emojize(f'{a}jogador:{f} pedra:raised_fist:\n{v}Bot:{f} tesoura:victory_hand:\nO {a}jogador{f} ganhou!'))#jogador
        print('='*20)
    elif j=='tesoura' and b=='pedra':
        print('='*20)
        print(emojize(f'{a}jogador:{f} tesoura:victory_hand:\n{v}Bot:{f} pedra:raised_fist:\nO {v}Bot{f} ganhou!'))#bot
        print('='*20)
    elif j=='papel' and b=='tesoura':
        print('='*20)
        print(emojize(f'{a}jogador:{f} papel:raised_back_of_hand:\n{v}Bot:{f} tesoura:victory_hand:\nO {v}Bot{f} ganhou!'))#bot
        print('='*20)
    else:
        print('='*20)
        print(emojize(f'{a}jogador:{f} {j}\n{v}Bot:{f} {b}\n{r}Empate!:handshake:{f}'))
        print('='*20)



    

