"""
72. Peça 5 números ao usuário, guarde em uma lista e mostre a lista completa.
"""
numeros = []
for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(f"{numero:.2f}")
print("Lista completa:", numeros)
