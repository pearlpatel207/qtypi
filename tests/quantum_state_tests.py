import numpy as np
from qtypi.quantum_state import QuantumState
from qtypi.gates import X_GATE

def test_initialization():
    qstate = QuantumState("0")
    assert np.allclose(qstate.state, np.array([[1], [0]], dtype=complex))

def test_apply_gate():
    qstate = QuantumState("0")
    qstate.apply_gate(X_GATE)
    assert np.allclose(qstate.state, np.array([[0], [1]], dtype=complex))

def test_measurement():
    qstate = QuantumState([1/np.sqrt(2), 1/np.sqrt(2)])
    result = qstate.measure()
    assert np.isclose(result['0'], 0.5)
    assert np.isclose(result['1'], 0.5)
