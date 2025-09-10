import math

HISTORICO_ARQUIVO = "historico-operacoes.txt"

def registrar_operacao(tipo_operacao, entrada1, entrada2, resultado):
    with open(HISTORICO_ARQUIVO, "a") as f:
        f.write(f"{tipo_operacao:<30} {entrada1:15.6f} {entrada2:15.6f} {resultado:15.6f}\n")

def duas_entradas():
    while True:
        try:
            entrada1 = float(input("Digite o primeiro número: "))
            entrada2 = float(input("Digite o segundo número: "))
            return entrada1, entrada2
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def entrada_unica(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

def calculadora():
    fim = False
    while not fim:
        print("\n--- CALCULADORA CIENTÍFICA PYTHON ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Potência")
        print("7. Logaritmo Natural")
        print("8. Seno")
        print("9. Cosseno")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            tipo_operacao = "Soma"
            entrada1, entrada2 = duas_entradas()
            resultado = entrada1 + entrada2
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, entrada2, resultado)

        elif opcao == '2':
            tipo_operacao = "Subtração"
            entrada1, entrada2 = duas_entradas()
            resultado = entrada1 - entrada2
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, entrada2, resultado)

        elif opcao == '3':
            tipo_operacao = "Multiplicação"
            entrada1, entrada2 = duas_entradas()
            resultado = entrada1 * entrada2
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, entrada2, resultado)

        elif opcao == '4':
            tipo_operacao = "Divisão"
            entrada1, entrada2 = duas_entradas()
            if entrada2 == 0:
                print("Erro: Divisão por zero.")
            else:
                resultado = entrada1 / entrada2
                print(f"Resultado: {resultado}")
                registrar_operacao(tipo_operacao, entrada1, entrada2, resultado)

        elif opcao == '5':
            tipo_operacao = "Raiz Quadrada"
            entrada1 = entrada_unica("Digite o número: ")
            if entrada1 < 0:
                print("Erro: Número negativo.")
            else:
                resultado = math.sqrt(entrada1)
                print(f"Resultado: {resultado}")
                registrar_operacao(tipo_operacao, entrada1, 0.0, resultado)

        elif opcao == '6':
            tipo_operacao = "Potência"
            entrada1, entrada2 = duas_entradas()
            # Calcula entrada1 elevado a entrada2
            resultado = math.exp(math.log(entrada1) * entrada2) if entrada1 > 0 else entrada1 ** entrada2
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, entrada2, resultado)

        elif opcao == '7':
            tipo_operacao = "Logaritmo Natural"
            entrada1 = entrada_unica("Digite o número: ")
            if entrada1 <= 0:
                print("Erro: Valor <= 0.")
            else:
                resultado = math.log(entrada1)
                print(f"Resultado: {resultado}")
                registrar_operacao(tipo_operacao, entrada1, 0.0, resultado)

        elif opcao == '8':
            tipo_operacao = "Seno"
            entrada1 = entrada_unica("Digite o ângulo (radianos): ")
            resultado = math.sin(entrada1)
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, 0.0, resultado)

        elif opcao == '9':
            tipo_operacao = "Cosseno"
            entrada1 = entrada_unica("Digite o ângulo (radianos): ")
            resultado = math.cos(entrada1)
            print(f"Resultado: {resultado}")
            registrar_operacao(tipo_operacao, entrada1, 0.0, resultado)

        elif opcao == '0':
            fim = True
            print("Calculadora encerrada.")

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    calculadora()
