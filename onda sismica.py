import math

def distancia_onda_sismica(): 
    print("=== Calculadora de Distäncia de Onda Sísmica ===")

    tipo_onda = input("Digite o tipo de onda(P,S,etc): ").upper()
    
    v = float(input("Velocidade de onda (m/s): "))

    t = float(input("Tempo (s): "))

    grau = float(input("Angulo de incidencia em graus (0 para vertical): ")) 

    rad = math.radians(grau)

    d_total = v * t

    d_horizontal = d_total * math.sin(rad)

    print("\n=== Resultado ---")
    print(f"Tipo de onda: {tipo_onda}")
    print(f"Distancia total percorrida: {d_total:.2f}m")
    print(f"Distancia horizontal: {d_horizontal:.2f}m (angulo {grau} )")

distancia_onda_sismica()

    