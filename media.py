qtd = int(input("Qtd notas: "))
notas = [float(input("Nota: ")) for _ in range(qtd)]
print("Média:", sum(notas)/qtd)