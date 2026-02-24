import numpy as np
#adicion de vectores complejos 
v1 = np.array([1+2j, 3+4j])
v2 = np.array([5+6j, 7+8j])

suma_vectores = v1 + v2
print("Suma de vectores:", suma_vectores)

#Inverso aditivo de un vector complejo
inverso_v1 = -v1
print("Inverso aditivo:", inverso_v1)

#Multiplicación de escalar por vector complejo
escalar = 2 + 1j
producto_escalar_vector = escalar * v1
print("Escalar por vector:", producto_escalar_vector)

#Adición de matrices complejas
A = np.array([[1+1j, 2+2j],
              [3+3j, 4+4j]])

B = np.array([[5+1j, 6+2j],
              [7+3j, 8+4j]])

suma_matrices = A + B
print("Suma de matrices:\n", suma_matrices)

#Inverso aditivo de una matriz compleja
inversa_aditiva_A = -A
print("Inversa aditiva:\n", inversa_aditiva_A)

#Multiplicación escalar por matriz compleja
producto_escalar_matriz = escalar * A
print("Escalar por matriz:\n", producto_escalar_matriz)

#Transpuesta de matriz/vector
print("Transpuesta de A:\n", A.T)
print("Transpuesta de v1:\n", v1.T)

#Conjugada de matriz/vector
print("Conjugada de A:\n", np.conjugate(A))
print("Conjugada de v1:\n", np.conjugate(v1))

#Adjunta (Daga) de matriz/vector
adjunta_A = A.conj().T
print("Adjunta (daga) de A:\n", adjunta_A)

#Producto de dos matrices compatibles
producto_matrices = np.matmul(A, B)
print("Producto de matrices:\n", producto_matrices)

#Acción de una matriz sobre un vector
def accion_matriz_vector(M, v):
    return np.matmul(M, v)

accion = accion_matriz_vector(A, v1)
print("Acción de A sobre v1:\n", accion)

#Producto interno de dos vectores
producto_interno = np.vdot(v1, v2)
print("Producto interno:", producto_interno)

#Norma de un vector
norma_v1 = np.linalg.norm(v1)
print("Norma de v1:", norma_v1)

#Distancia entre dos vectores
distancia = np.linalg.norm(v1 - v2)
print("Distancia entre v1 y v2:", distancia)

#Valores y vectores propios
valores_propios, vectores_propios = np.linalg.eig(A)

print("Valores propios:\n", valores_propios)
print("Vectores propios:\n", vectores_propios)

#Verificar si una matriz es Unitaria
def es_unitaria(U):
    identidad = np.eye(U.shape[0])
    return np.allclose(U @ U.conj().T, identidad)

print("¿A es unitaria?", es_unitaria(A))

#Verificar si una matriz es Hermitiana
def es_hermitiana(M):
    return np.allclose(M, M.conj().T)

print("¿A es Hermitiana?", es_hermitiana(A))

#Producto tensor
tensor_matrices = np.kron(A, B)
print("Producto tensor A ⊗ B:\n", tensor_matrices)

tensor_vectores = np.kron(v1, v2)
print("Producto tensor v1 ⊗ v2:\n", tensor_vectores)
