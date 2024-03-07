#desafio 019
from random import choice
aluno = input('Digite o nome do  primeiro Aluno: ')
aluno2 = input('Digite o nome do segundo Aluno: ')
aluno3 = input('Digite o nome do  terceiro Aluno: ')
aluno4 = input('Digite o nome do  quarto Aluno: ')
sorteador = choice([aluno, aluno2, aluno3, aluno4])
print(f'O escolhido para apagar o quadro é: {sorteador}')
