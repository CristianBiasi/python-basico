"""
76. Crie uma lista de compras vazia. Peça 5 itens ao usuário e adicione cada item na lista.
"""
compras = []
for i in range(5):
    itens = str(input("Digite 5 itens para sua lista de compras."))
    compras.append(itens)
print(compras)