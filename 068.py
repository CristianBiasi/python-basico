"""
68. Mostre os 10 primeiros números da sequência de Fibonacci.
"""
n = int(input("Digite até qual termo da sequencia de Fibonacci vc quer exibir"))
t1 = 0
t2 = 1

for i in range(n):
    print(t1, end=' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3