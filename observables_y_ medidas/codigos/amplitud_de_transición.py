import numpy as np

def transition_amplitude(phi, psi):
    return np.vdot(phi, psi)

def transition_probability(phi, psi):
    return np.abs(transition_amplitude(phi, psi))**2