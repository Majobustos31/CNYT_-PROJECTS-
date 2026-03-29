import numpy as np
#4.3.1
def valor_esperado(probabilidades, eigenvalores):
    return sum(p * l for p, l in zip(probabilidades, eigenvalores))

#4.3.2
p = [0.5, 0.5]
lambdas = [1, -1]

media = valor_esperado(p, lambdas)
print("Valor esperado:", media)

#4.4.1
def es_unitaria(U):
    U = np.array(U, dtype=complex)
    identidad = np.eye(len(U))
    producto = np.dot(U, U.conj().T)
    return np.allclose(producto, identidad)

#Pruebas de enunciado 
U1 = np.array([
    [0,1],
    [1,0]
])

U2 = np.array([
    [1/np.sqrt(2), 1/np.sqrt(2)],
    [1/np.sqrt(2), -1/np.sqrt(2)]
])

print("U1 es unitaria:", es_unitaria(U1))
print("U2 es unitaria:", es_unitaria(U2))

# Producto
producto = np.dot(U1, U2)
print("Producto es unitaria:", es_unitaria(producto))

#4.4.2
import numpy as np

# Estado inicial |00>
psi0 = np.array([1, 0, 0, 0], dtype=complex)

# Operador U
sqrt2 = np.sqrt(2)
U = np.array([
    [0, 1/sqrt2, 1/sqrt2, 0],
    [1/sqrt2, 0, 0, 1/sqrt2],
    [1/sqrt2, 0, 0, -1/sqrt2],
    [0, 1/sqrt2, -1/sqrt2, 0]
], dtype=complex)

def evolve(U, psi, steps):
    for _ in range(steps):
        psi = U @ psi
    return psi

# Evolución
psi3 = evolve(U, psi0, 3)

# Probabilidad de |01> (índice 1)
prob_01 = abs(psi3[1])**2

print("Estado final:", psi3)
print("Probabilidad de |01>:", prob_01)