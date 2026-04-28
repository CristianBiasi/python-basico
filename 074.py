"""
74. Peça 5 números ao usuário e mostre apenas os números pares.
"""
"""
numeros = []
numeros_pares = []
for i in range(5):
    num = float(input(f"Digite o número 0{i+1}/05, será exibido somente os pares "))
    num = int(num)
    numeros.append(num)

for p in numeros:
    if p % 2 == 0:
        numeros_pares.append(p)
print("Lista de números pares", numeros_pares)
"""
numeros_pares = []

for i in range(5):
    num = int(input(f"Digite o número {i+1}/5: "))
    
    if num % 2 == 0:
        numeros_pares.append(num)

print("Lista de números pares:", numeros_pares)