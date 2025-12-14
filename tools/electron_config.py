from .orbitals import ORBITALS

def electron_configuration(atomic_number):
    electrons_left = atomic_number
    configuration = []

    for subshell, orbital_count in ORBITALS:
        if electrons_left <= 0:
            break

        max_electrons = orbital_count * 2
        electrons_in_subshell = min(electrons_left, max_electrons)
        electrons_left -= electrons_in_subshell

        orbitals = [0] * orbital_count

        # Hund's rule: fill ↑ first
        for i in range(orbital_count):
            if electrons_in_subshell > 0:
                orbitals[i] += 1
                electrons_in_subshell -= 1

        # Then fill ↓
        for i in range(orbital_count):
            if electrons_in_subshell > 0:
                orbitals[i] += 1
                electrons_in_subshell -= 1

        configuration.append({
            "subshell": subshell,
            "orbitals": orbitals
        })

    return configuration
