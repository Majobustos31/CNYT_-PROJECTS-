import numpy as np
import matplotlib.pyplot as plt

# Estado inicial
estado_inicial = np.array([1,0,0,0,0,0,0,0], dtype=complex)

# Matriz cuántica (con números complejos)
M = np.array([
    [0,0,0,0,0,0,0,0],
    [1/np.sqrt(2),0,0,0,0,0,0,0],
    [1/np.sqrt(2),0,0,0,0,0,0,0],
    [0,-1/np.sqrt(6),1/np.sqrt(6),0,0,0,0,0],
    [0,1/np.sqrt(6),1/np.sqrt(6),0,0,0,0,0],
    [0,-1/np.sqrt(6),1/np.sqrt(6),0,0,0,0,0],
    [0,1/np.sqrt(6),-1/np.sqrt(6),0,0,0,0,0],
    [0,1/np.sqrt(6),1/np.sqrt(6),0,0,0,0,0],
], dtype=complex)

# Evolución
estado_1 = np.dot(M, estado_inicial)
estado_final = np.dot(M, estado_1)

# Probabilidades (módulo al cuadrado)
probabilidades = np.abs(estado_final)**2

print("Resultado final:", probabilidades)

# Graficar
plt.bar(range(len(probabilidades)), probabilidades)
plt.title("Experimento cuántico")
plt.xlabel("Posición")
plt.ylabel("Probabilidad")
plt.show()