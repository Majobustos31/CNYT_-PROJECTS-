import nunpy as np
def eigen_probabilities(A, psi):
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    
    probs = []
    for i in range(len(eigenvalues)):
        vec = eigenvectors[:, i]
        prob = np.abs(np.vdot(vec, psi))**2
        probs.append(prob)
    
    return eigenvalues, probs