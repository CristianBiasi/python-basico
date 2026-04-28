"""
65. Peça uma senha ao usuário até que ele digite a senha correta.
"""
senha = str(input("Cadastre uma senha: "))
senhaVerificacao = str(input("Confirme sua senha: ")) 
while senhaVerificacao != senha:
    senhaVerificacao = str(input("Confirme sua senha: ")) 
else:
    print("Senha confirmada!")