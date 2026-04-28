"""
73. Peça 5 números ao usuário e mostre o maior e o menor valor da lista.
"""
numeros = []
for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(f"{numero:.2f}")

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
