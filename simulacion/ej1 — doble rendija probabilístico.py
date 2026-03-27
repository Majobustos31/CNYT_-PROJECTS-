import numpy as np
import matplotlib.pyplot as plt

estado_inicial = np.array([1,0,0,0,0,0,0,0])

M = np.array([
    [0,0,0,0,0,0,0,0],
    [1/2,0,0,0,0,0,0,0],
    [1/2,0,0,0,0,0,0,0],
    [0,1/3,0,0,0,0,0,0],
    [0,1/3,0,0,0,0,0,0],
    [0,1/3,0,0,0,0,0,0],
    [0,0,1/3,0,0,0,0,0],
    [0,0,1/3,0,0,0,0,0],
])

estado_1 = np.dot(M, estado_inicial)
estado_final = np.dot(M, estado_1)
print("Resultado final:", estado_final)

plt.bar(range(len(estado_final)), estado_final)
plt.title("Experimento probabilístico")
plt.xlabel("Posición")
plt.ylabel("Probabilidad")
plt.show()