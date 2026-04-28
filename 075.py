"""
75. Peça 5 números ao usuário e mostre a soma dos valores da lista.
"""
"""
numeros = []
c = 0
for i in range(5):
    num = int(input(f"Digite o número {i+1} de 5. "))
    c = c + num
    numeros.append(num)

print(f"Soma nos numeros eh {c}\nListe é números digitados eh {numeros}")
"""
numeros = []

for i in range(5):
    num = int(input(f"Digite o número {i+1} de 5. "))
    numeros.append(num)

print(f"Soma nos numeros eh {sum(numeros)}\nListe é números digitados eh {numeros}")