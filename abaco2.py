def mostrar_abaco(valores, max_contas=10):
    for nivel in range(max_contas, 0, -1):
        linha = ''
        for valor in valores:
            if valor >= nivel:
                linha += ' o '
            else:
                linha += ' | '
        print(linha)
    print('---' * len(valores))
    print(' '.join(str(v) for v in valores))


def alterar_abaco():
    colunas = [0] * 5
    while True:
        mostrar_abaco(colunas)
        print("Digite 'sair' para encerrar.")
        entrada = input("Escolha a coluna (0 a 4): ")
        if entrada.lower() == 'sair':
            break
        try:
            idx = int(entrada)
            valor = int(input("Novo valor (0 a 10): "))
            if 0 <= idx < len(colunas) and 0 <= valor <= 10:
                colunas[idx] = valor
            else:
                print("Entrada inválida.")
        except ValueError:
            print("Erro de entrada.")
        print()


alterar_abaco()