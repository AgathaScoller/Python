frase = input("Frase: ").lower()
cont = 0
for l in frase:
    if l in "aeiou": cont += 1
print("Vogais:", cont)