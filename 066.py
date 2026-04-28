"""
66. Peça um número inteiro positivo e calcule o fatorial dele.
"""

# Validação da entrada
entrada = input("Digite um número inteiro positivo para saber seu fatorial: ")

# Verifica se é número inteiro
if not entrada.isdigit():
    print("Erro: você deve digitar apenas números inteiros positivos (sem letras ou decimais).")
else:
    entrada = int(entrada)

    if entrada < 0:
        print("Erro: o número deve ser positivo.")
    else:
        fatorial = 1
        print("\nCálculo do fatorial:")

        for i in (range(1, entrada + 1)):
            fatorial *= i
            print(f'{i}! = {fatorial} ')

        print(fatorial)

dificuldade = 2