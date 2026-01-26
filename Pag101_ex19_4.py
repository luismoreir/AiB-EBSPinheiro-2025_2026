import numpy as np
import matplotlib.pyplot as plt
import math

# Gerar valores de x entre 0 e 5, com passo 0.01
x = np.arange(0, 2*math.pi, 0.01)
y = np.sin(x)
y1 = np.cos(x)
#y2 = np.tan(x)
#y3 = 1/np.tan(x)
# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(x,y, label='sen(x)', color='blue')
plt.plot(x,y1, label='cos(x)', color='red')
plt.ylim(-1.5, 1.5)
#plt.plot(x,y2, label='tan(x)', color='green')
#plt.plot(x,y3, label='cotan(x)', color='orange')
plt.legend()
plt.title("Gráfico da função seno e coseno de x")
plt.xlabel("x")
plt.ylabel("sen(x) e cos(x)")
plt.grid(True)
plt.show()