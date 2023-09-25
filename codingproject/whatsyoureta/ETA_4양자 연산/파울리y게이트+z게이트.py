import matplotlib.pyplot as plt

from math import pi

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit.tools.visualization import circuit_drawer
from qiskit.quantum_info import state_fidelity
from qiskit import BasicAer

qc = QuantumCircuit(1)
qc.y(0)
qc.z(0)
qc.draw('mpl')