while True:
    op = int(input("\n1-Somar 2-Subtrair 0-Sair: "))
    if op == 1: a,b = map(float,input("Dois números: ").split()); print("Soma:", a+b)
    elif op == 2: a,b = map(float,input("Dois números: ").split()); print("Subtração:", a-b)
    elif op == 0: break
    else: print("Inválido")