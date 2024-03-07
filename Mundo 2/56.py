#desafio 056
soma_idade = 0
idade_homem = 0
mulher=0
for c in range(1, 5):
    nome = str(input(f'\033[35mDigite o\033[m \033[32m{c}°\033[m \033[35mnome ==>\033[m ')).strip().lower().title()
    idade = int(input(f'\033[35mDigite a idade ==>\033[m '))
    sexo = str(input(f'\033[35mDigite o gênero (F/M) ==>\033[m ')).upper().strip()
    idade = soma_idade + idade
    if sexo =='M' and idade > idade_homem:
        nome_homem= nome
        idade_homem = idade
    if sexo =='F' and idade < 20:
        mulher = mulher+1
print(f'A média das idades do grupo é de \033[32m{idade/4:.1f}\033[m anos.')
print(f'O homem mais velho é \033[34m{nome_homem}\033[m, com \033[32m{idade_homem}\033[m anos.')
print(f'\033[35m{mulher}\033[m das mulheres inseridas tem menos de 20 anos.')

