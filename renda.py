renda = float(input("Digite sua renda mensal: "))
restricao = input("Você possui restrição no nome? (sim ou não): ")

if renda > 5000 and restricao == "não":
    print("Empréstimo aprovado.")
else:
    print("Empréstimo não aprovado.")