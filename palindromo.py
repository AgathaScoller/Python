mensagem = input("Digite uma palavra:")
palavra = mensagem.replace(" ","").lower()

texto_final = ""
for caractere in palavra:
    texto_final = caractere + texto_final

if mensagem == texto_final:
    print("Essa palavra é um palindromo")
else:
    print("Essa palavra nao é um palindromo")
