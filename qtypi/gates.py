import numpy as np

# Pauli-X (bit-flip) gate
X_GATE = np.array([[0, 1], [1, 0]], dtype=complex)

# Pauli-Z gate
Z_GATE = np.array([[1, 0], [0, -1]], dtype=complex)

# Hadamard gate
H_GATE = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)

# Other gates can go here...

