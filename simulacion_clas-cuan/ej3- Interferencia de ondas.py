import numpy as np
import matplotlib.pyplot as plt

# Parámetros
distancia_rendijas = 0.5
longitud_onda = 0.1
distancia_pantalla = 1
ancho_pantalla = 2
num_puntos = 500

# Puntos en la pantalla
x = np.linspace(-ancho_pantalla/2, ancho_pantalla/2, num_puntos)

# Distancias a cada rendija
r1 = np.sqrt((x - distancia_rendijas/2)**2 + distancia_pantalla**2)
r2 = np.sqrt((x + distancia_rendijas/2)**2 + distancia_pantalla**2)

# Ondas
k = 2 * np.pi / longitud_onda

onda1 = np.cos(k * r1)
onda2 = np.cos(k * r2)

# Superposición
onda_total = onda1 + onda2

# Intensidad
intensidad = onda_total**2

# Gráfica
plt.figure(figsize=(10,5))
plt.plot(x, intensidad)
plt.title("Patrón de interferencia (doble rendija)")
plt.xlabel("Posición")
plt.ylabel("Intensidad")
plt.show()