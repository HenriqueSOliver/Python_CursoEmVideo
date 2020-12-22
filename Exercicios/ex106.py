'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
 a palavra 'FIM', o programa se encerrará. Importante: use cores.'''

c = ('\033[m', #0-sem cores
'\033[0;30;41m', #1-vermelho
'\033[0;30;42m', #2-verde
'\033[0;30;43m', #3-amarelo
'\033[0;30;44m', #4 -azul
'\033[0;30;45m', #5-roxo
'\033[7;30m' #6-branco
)

def ajuda(com):
    help(com)

def tit(msg, cor=1):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~'* tam)
    print(c[0], end='')


#Programa principal

comando = ''
while True:
    tit('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
tit('ATÉ LOGO!', 1)