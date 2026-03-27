def evolve_state(psi, operators):
    state = psi.copy()
    for U in operators:
        state = U @ state
    return state