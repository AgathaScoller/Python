mensagem = input("Digite um texto:")

texto_final = ""
for caractere in mensagem: 
    texto_final = caractere + texto_final
print(texto_final)
