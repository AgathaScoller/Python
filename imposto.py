salario = float(input("Digite seu salário: "))

if salario <= 2000:
    imposto = 0
elif salario <= 3000:
    imposto = salario * 0.10
elif salario <= 5000:
    imposto = salario * 0.15
else:
    imposto = salario * 0.20

print(f"Imposto a pagar: R$ {imposto:.2f}")