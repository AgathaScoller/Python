import string

alfabeto = list(string.ascii_uppercase)

while True:
    entrada = input("Digite uma letra (A-Z) ou número (1-26) ou 'sair'para encerrar: ").strip().upper()
    if  entrada == "SAIR":
        print("Encerrando programa...")
        break
    if entrada.isalpha() and len() == 1:
        if entrada in alfabeto:
            posicao = alfabeto.index(entrada)+1
            print(f"A letra '{entrada}' é a {posicao} do alfabeto")
        else:
            print("Letra Inexistente")
    elif entrada.isdigit():
        numero = int(entrada)
        if 1 <= numero <= 26:
            print(f"O numero {numero} corresponde a letra {alfabeto[numero-1]}.")
        else:
            print("Numero Inexistente")




