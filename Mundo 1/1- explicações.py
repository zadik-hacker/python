#ATALHOS

#Duplicar Linha = Shift + Alt + Seta
#Mover Linha = Alt + Seta
#Apagar Linha = Ctrl + Shift + K
#Multi Ocorrências = Ctrl + D
#Multi Seleção = Alt + Click
#Zen Mode = Ctrl + K Z
#IntelliSense = Ctrl + Espaço

#ESTRUTURA DE REPETIÇÃO 
'''
for = laço
c = variavel ( com o numero de iteração dentro do loop ou laço)
in = no
range() = intervalo  '''

# ( o 'c' dentro do laço seria a repetição da variavel de 1 ate 10, nunca esquecer os dois pontos no final)
#       for c in range(1,10):
#           passo
#       pega

#(inves de criar 3 passo pula, crio um laço para pular tres vezes e no final ele anda e pega)
#for c in range(0,3):    
#    passo
#    pula
#passo
#pega

# (com uma condição seria assim dentro do laço usando if)
#for c in range(0,3):
#   if moeda:
#       pega    
#  passo
#  pula
#passo
#pega

# != ( sinal de diferente com  o if)
# += ( sinal de atribuição)
# abs() numero absoluto tirar do negativo
 
#CORES PARA TERMINAL PYTHON ANSI
#text     color        background
 
# 30      black         preto      40
# 31      red           vermelho   41
# 32      green         verde      42
# 33      yellow        amarelo    43
# 34      blue          azul       44
# 35      Magenta       Magenta    45
# 36      cyan          ciano      46
# 37      grey          cinza      47
# 97      white         branco     107


# not in   ====> é um operador em Python que verifica se um valor não está presente em uma sequência (como uma lista, tupla, string, etc.)

#exemplo = exercicio 45

#jv = ['pedra','papel', 'tesoura']
#if j not in jv:
   # print('Escolha não permitida, use apenas pedra - papel ou tesoura!!')


#Ordem de Precendência

#1- ()
#2- **
#3- * / // %
#4- + -

#-~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

 #   + -> Adição              ** -> Potencia
 #   - -> Subtração           // -> Divisão inteira
 #   * -> Multiplicação        % -> Resto da divisão
 #   / -> Divisão 

#Codição 

#   ==  , e sinal de igual no python 

#if carro.esquerdo():
#     bloco True
#else:
#     bloco False

#exemplo

carro = int(input('Digite o ano do carro: '))
if carro <=3:
    print('carro novo') #caminho verde
else:
    print('carro velho klkkkkfskfsafhjskfja') #caminho vermelho
print('--fim--')

#exemplo



#tipos primitivo

#Inteiro - int -> Numeros inteiros( -2,-1,1,2,3,4....)

#Real, Ponto futuante - float -> Numeros com casas decimais(2.56)

#Booleano - bool -> verdadeiro ou falso (true, false)

#String - str -> textos alfanumericos("o rato roeu a roupa do rei")

# type() ---> Indica o tipo primitivo da var ->  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string



# MODULOS

#math
# - ceil ( arredonda para cima)
# - floor ( arredonda para baixo)
# - trunc (vai truncar o numero, elimina a virgula, sem arredondamento)
# - pow (potencia, expoente) - hipotenusa = math.sqrt(math.pow(cateto, 2) + math.pow(cateto2, 2)) elevado ao quadrado e calculando logo a raiz em seguida dos outros cateto
# - sqrt (raiz quadrada)
# - factorial ( calculo fatorial)

 # from math import cos -> Importa somente a funçao cos da biblioteca math

  # math -> Biblioteca de operadores aritméticos {

     # sqrt()  ---> Raiz Quadrada de um numero ------- raiz = math.sqrt(numero)
     # floor() ---> Arredonda o numero para baixo ---- 5,23 fica 5,00
     # ceil() -----> Retorna um valor inteiro ---------------- 5,23 fica 5
     # hypot() ---> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     # pow() ----> Potencia de um numero ---------------- pow(2, 3) = 2³ = 8
     # radians()-> Converte em graus radianos ---------- print(math.radians(180))
     # cos() -----> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     # sin() ------> Retorne o seno em radianos --------- print(math.sin(math.radians(x)))
     # tan() -----> Retorne a tangente em radianos---- print(math.tan(math.radians(x)))

# random -> Gerar numeros pseudoaleatorios 

      # randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      # choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      # shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)




# Manipulando Textos 

#frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'

   #FATIAMENTO
  # frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
  # frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
  # frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA

  # ANALISE

  # len() -------------> Mostra quantas letras tem a frase -------------------------------- len(frase) = 38 letras
  # count() ---------> Conta quantas vezes aparece a letra escolhida ----------- frase.count('s')
  # find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')


   #TRANSFORMAÇOES
   
  # replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript') no caso para espaços seria frase.replace(' ', '')
  # upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
  # lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
  # capitalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
  # title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
  # strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
  # split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
  # .join() -----------> Juntar uma coisa com a outra -------------------------------------- ', '.join(frase) Estou-aprendendo-a-programar-em-python

#isalnum – Verifique se todos os caracteres no texto são alfanuméricos
#isalpha – Verifique se todos os caracteres no texto são letras
#isascii – Verifique se a sequência é composta por todos os caracteres ASCII ou se a sequência estiver vazia também retornara true
#isdecimal – Verifique se todos os caracteres no objeto unicode são decimais
#isdigit – Verifique se todos os caracteres no texto são dígitos
#isidentifier – Verifique se a sequência é um identificador válido :: O método isidentifier () retornará True se a string for um identificador válido, caso contrário, False. Uma sequência é considerada um identificador válido se contiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). Um identificador válido não pode começar com um número ou conter espaços.
#islower – Verifique se todos os caracteres do texto estão em minúsculas
#isnumeric – Verifique se todos os caracteres no texto são numéricos
#isprintable – Verifique se todos os caracteres no texto são imprimíveis
#isspace – Verifique se todos os caracteres no texto são espaços em branco
#istitle – Verifique se cada palavra começa com uma letra maiúscula
#isupper – Verifique se todos os caracteres do texto estão em maiúsculas