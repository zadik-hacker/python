#desafio 062
t = int(input('Digite o primeiro termo: ')) #t2 ultimo , #t = termo                                            #
r = int(input('Digite a razão: '))          #progressao aritmetica (pa)
ut = int(input('Digite o ultimo termo: '))  #ultimo termo(ut), #(o) = opão
pa = t + ((ut + 1) - 1) * r
t2 = pa

while t != t2:
    t += r
    print(f'\033[m\033[3{r}m{t}\033[m')
    if t == t2:
        o = str(input('Digite [SIM] ou [S] se deseja mais, [NAO] ou [N] para encerrar o programa: ')).upper()
        if o == 'S' or o == 'SIM':
            s = int(input('Quanto você quer ver mais?==> '))
            t2 += s * r
            if t == t2:
                t2 = t
        else:
            t = t2
print('\033[1;31mObrigado por ter usado a aplicação❤️\033[m')
