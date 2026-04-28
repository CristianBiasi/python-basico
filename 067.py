"""
67. Peça um número inteiro e informe se ele é primo.
"""
num = int(input("Digite um número inteiro para saber se ele é um numero primo "))
'''
O que é um número primo ?
7 ele é divisivel por 1 e por ele mesmo.
'''
if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    print('Nao eh primo')
else:
    print(f'{num} eh primo')