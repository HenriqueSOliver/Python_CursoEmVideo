'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

n = (int(input('Digite número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite p último número: ')))

print(f'Você digitou os valores {n}')

print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram:', end='')
for num in n:
    if num % 2 == 0:
        print(n, end=' ')