peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))

imc = (peso/(altura**2))


print("Calculadora de IMC","\npeso",peso,"\naltura",altura,f"\nimc {imc:.2f}")
print("Seu IMC está adequado?",imc >=18.5 and imc <= 24.9)

