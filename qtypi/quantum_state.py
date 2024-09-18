import numpy as np

class QuantumState:
    def __init__(self, state):
        """
        Initialize the quantum state.
        Accepts:
        - A string representing a computational basis state (e.g., '0', '1', '00', '11')
        - A list or numpy array representing a superposition state
        """
        if isinstance(state, str):
            self.state = self._initialize_state_from_string(state)
        elif isinstance(state, (list, np.ndarray)):
            self.state = self._initialize_state_from_vector(state)
        else:
            raise ValueError("State must be a string (e.g., '0', '1', '01') or a list/array of amplitudes.")
    
    def _initialize_state_from_string(self, state: str) -> np.ndarray:
        """Converts a string like '0', '1', '00', '11' into a quantum state vector."""
        if not all(c in '01' for c in state):
            raise ValueError("State must consist only of '0' and '1'")

        # Determine the number of qubits
        num_qubits = len(state)

        # Start with a 2^num_qubits size zero vector
        state_vector = np.zeros((2**num_qubits, 1), dtype=complex)

        # Find the index corresponding to the binary string
        index = int(state, 2)
        state_vector[index] = 1.0

        return state_vector
    
    def _initialize_state_from_vector(self, vector) -> np.ndarray:
        """Initializes the state from a list or array of amplitudes."""
        vector = np.array(vector, dtype=complex).reshape(-1, 1)
        
        # Normalize the state vector to ensure the norm is 1
        norm = np.linalg.norm(vector)
        if norm == 0:
            raise ValueError("State vector cannot have norm 0.")
        return vector / norm
    
    def apply_gate(self, gate: np.ndarray):
        """Applies a quantum gate (as a matrix) to the state."""
        self.state = np.dot(gate, self.state)
    
    def measure(self):
        """Measures the quantum state and returns probabilities."""
        probabilities = np.abs(self.state)**2
        result = {}
        num_qubits = int(np.log2(len(probabilities)))

        # Generate binary labels for measurement outcomes
        for i in range(2**num_qubits):
            result[bin(i)[2:].zfill(num_qubits)] = probabilities[i][0]

        return result

    def __repr__(self):
        return f"QuantumState: {self.state}"

# Example usage with a superposition state

# Create the superposition state 1/sqrt(2) * (|0> + |1>)
superposition_state = QuantumState([1/np.sqrt(2), 1/np.sqrt(2)])
print(superposition_state)

# Measure the superposition state
measurement = superposition_state.measure()
print("Measurement results:", measurement)
