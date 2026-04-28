"""
70. Peça uma palavra e conte quantas vogais ela possui.
"""
palavra = str(input("Digite um palavra para saber quantas vogais tem "))
vogal = ["a","e","i","o","u"]
palavra = palavra.lower() # para deixar tudo minusculo e facilitar a comparação

c = 0
for l in palavra:
    if l in vogal:
        c += 1
        print(f'Vogal: {l} - Total de vogais: {c}')