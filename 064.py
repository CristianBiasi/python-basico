"""
64. Peça números ao usuário até que ele digite `0`. No final, mostre a soma dos números digitados.
"""
n = float(input("digite um numero, até vc digitar 0 ele somará os anteriores "))
c = 0
while n != 0:
    c += n
    n = float(input(f'Valor atual {c}\nNúmero digitado {n}\nDigite outro numero\n{30*"="} '))
print(c)