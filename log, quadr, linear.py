import matplotlib.pyplot as plt
import numpy as np

# Funções
def lin(x):
    return 2*x + 3

def qua(x):
    return x**2

def log(x):
    return np.log(x)  

def exp(x):
    return 2**x  

x_linear = np.linspace(-10, 10, 200)
x_quad = np.linspace(-10, 10, 200)
x_log = np.linspace(0.1, 10, 200)  
x_exp = np.linspace(-5, 5, 200)     

y_linear = lin(x_linear)
y_quad = qua(x_quad)
y_log = log(x_log)
y_exp = exp(x_exp)

plt.figure(figsize=(8, 5))

plt.plot(x_linear, y_linear, label="lin(x) = 2x + 3", color="blue")
plt.plot(x_quad, y_quad, label="qua(x) = x^2", color="red")
plt.plot(x_log, y_log, label="log(x) = ln(x)", color="green")
plt.plot(x_exp, y_exp, label="exp(x) = 2^x", color="orange")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, linestyle="--", alpha=0.6)

plt.title("Funções Afim, Quadrática, Logarítmica e Exponencial")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
