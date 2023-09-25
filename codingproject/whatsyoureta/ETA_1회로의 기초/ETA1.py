import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram




# Create a Quantum Circuit
qc = QuantumCircuit(3, 3)
qc.barrier(range(3))
# map the quantum measurement to the classical bits
qc.measure(range(3), range(3))

# The Qiskit circuit object supports composition.
# Here the meas has to be first and front=True (putting it before)
# as compose must put a smaller circuit into a larger one.
qc = qc.compose(qc, range(3), front=True)

#drawing the circuit
qc.draw('mpl')

# Use AerSimulator


backend = AerSimulator()

# First we have to transpile the quantum circuit
# to the low-level QASM instructions used by the
# backend
qc_compiled = transpile(qc, backend)

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = backend.run(qc_compiled, shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()


counts = result_sim.get_counts(qc_compiled)
print(counts)
plot_histogram(counts)

#히스토그램 
plot_histogram(counts)



# Create a Quantum Circuit
meas = QuantumCircuit(3, 3)
meas.barrier(range(3))
# map the quantum measurement to the classical bits
meas.measure(range(3), range(3))

# The Qiskit circuit object supports composition.
# Here the meas has to be first and front=True (putting it before)
# as compose must put a smaller circuit into a larger one.
qc = meas.compose(qc, range(3), front=True)

#drawing the circuit
qc.draw('mpl')

# Use AerSimulator


backend = AerSimulator()

# First we have to transpile the quantum circuit
# to the low-level QASM instructions used by the
# backend
qc_compiled = transpile(qc, backend)

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = backend.run(qc_compiled, shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()


counts = result_sim.get_counts(qc_compiled)
print(counts)
plot_histogram(counts)

#히스토그램 
plot_histogram(counts)