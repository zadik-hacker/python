#desafio 040
from emoji import emojize #modulo de emoji
m1 = float(input('Digite a primeira nota do aluno: ')) #nota 1
m2 = float(input('Digite a segundo nota do aluno: ')) #nota 2
media = (m1+m2)/2 #calculo da media
if media <= 5.0:
    print(emojize(f'\033[31mVOCE FOI REPROVADO, TENTE MELHOR NA PROXIMA | MEDIA:{media} :sad_but_relieved_face:\033[m'))
elif media > 5.0 and media <=6.9:
    print(emojize(f'\033[34mVOCE ESTA DE RECUPERAÇÃO, BOA SORTE E ESTUDE | MEDIA:{media} \033[m:winking_face:'))
elif media >=7.00:
    print(emojize(f'\033[32mVOCE FOI APROVADO PARABENS!!! | MEDIA:{media} :birthday_cake::partying_face::party_popper:\033[m'))
    