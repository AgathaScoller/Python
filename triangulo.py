a = float(input("Digite o lado 1: "))
b = float(input("Digite o lado 2: "))
c = float(input("Digite o lado 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Os lados formam um triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Os lados formam um triângulo Isósceles.")
    else:
        print("Os lados formam um triângulo Escaleno.")
else:
    print("Os lados não podem formar um triângulo.")