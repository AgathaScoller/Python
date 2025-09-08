valor = int(input("Digite o valor do saque: "))

if valor % 10 == 0 and 10 <= valor <= 600:
    print(f"Saque de R$ {valor} liberado.")
else:
    print("Valor de saque inválido.")