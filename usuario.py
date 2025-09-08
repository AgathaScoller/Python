usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if (usuario == "admin" or usuario == "usuario") and senha == "senhacerta":
    print("Login sucedido.")
else:
    print("Falha no login.")