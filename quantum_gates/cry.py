from qiskit import CompositeGate
from qiskit import QuantumCircuit
from qiskit._instructionset import InstructionSet
from qiskit._quantumregister import QuantumRegister
from qiskit.extensions.standard import header  # pylint: disable=unused-import


class CryGate(CompositeGate):
    """Fredkin gate."""

    def __init__(self, theta, ctl, tgt, circ=None):
        """Create new Fredkin gate."""
        super().__init__("cry", [theta], [ctl, tgt], circ)
        self.cx(ctl, tgt)
        self.ry(-theta / 2, tgt)
        self.cx(ctl, tgt)
        self.ry(theta / 2, tgt)

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.cry(self.param[0], self.arg[0], self.arg[1]))


def cry(self, theta, ctl, tgt):
    """Apply Fredkin to circuit."""

    if isinstance(ctl, QuantumRegister) and \
       isinstance(tgt, QuantumRegister) and len(ctl) == len(tgt):
        instructions = InstructionSet()
        for i in range(ctl.size):
            instructions.add(self.cry(theta, (ctl, i), (tgt, i)))
        return instructions

    self._check_qubit(ctl)
    self._check_qubit(tgt)
    self._check_dups([ctl, tgt])

    return self._attach(CryGate(theta, ctl, tgt, self))


QuantumCircuit.cry = cry
CompositeGate.cry = cry
