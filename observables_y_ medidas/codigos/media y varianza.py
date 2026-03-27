import numpy as np
def is_hermitian(A):
    return np.allclose(A, A.conj().T)

def expectation_value(A, psi):
    return np.vdot(psi, A @ psi)

def variance(A, psi):
    exp_val = expectation_value(A, psi)
    exp_val_sq = expectation_value(A @ A, psi)
    return exp_val_sq - exp_val**2
