"""
77. Peça nomes ao usuário até ele digitar `sair`. Depois mostre todos os nomes cadastrados.
"""
users = []
while True:
    user = str(input("Digite nomes de usuarios, até digitar 'sair' para encerrar."))
    if user.lower() == 'sair':
        break
    users.append(user)
print(f"Usuarios cadastrados no sistema, {users}")