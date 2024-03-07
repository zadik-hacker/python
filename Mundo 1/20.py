#desafio 020
from random import shuffle
from emoji import emojize
aluno1 = str(input('Digite o nomes dos alunos(as) com virgula: ')).strip()
aluno_lista = aluno1.split(',')
sorteador = shuffle(aluno_lista)
print(emojize(f':nerd_face: ESTUDANTES :nerd_face:\n {aluno_lista}'))