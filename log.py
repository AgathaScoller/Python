import matplotlib.pyplot as plt
import numpy as np


def log(x):
    return np.log(x)  

x_log = np.linspace(0.1, 10, 200)  
y_log = log(x_log)


plt.figure(figsize=(8, 5))

plt.plot(x_log, y_log, color="green")
plt.title("Função Logarítmica: ln(x)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
