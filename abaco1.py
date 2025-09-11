def mostrar_abaco(valores, max_contas=10):
    for nivel in range(max_contas, 0, -1):  # De cima para baixo
        linha = ''
        for valor in valores:
            if valor >= nivel:
                linha += ' o '
            else:
                linha += ' | '
        print(linha)
    print('---' * len(valores))
    print(' '.join(str(v) for v in valores))

colunas = [3, 7, 2, 5, 9]  
mostrar_abaco(colunas)
