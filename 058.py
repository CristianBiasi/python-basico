"""
58. Peça um número e mostre a tabuada dele de 1 a 10.
"""
n = int(input("Digite um número par asaber sua tabuada."))
for i in range(1,11):
    print(f"{i} X {n} = {n*i}")