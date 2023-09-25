import numpy as np
from qiskit import *
from qiskit import Aer
from qiskit.visualization import plot_histogram


#회로 만들기
circ = QuantumCircuit(3)

#h게이트를 양자 큐빗 0에 추가
circ.h(0)
#CNOT 게이트를 제어 큐빗 0와 타겟 큐빗 1에 추가
#벨 상태에 있는 큐빗
circ.cx(0, 1)
#CNOT 게이트를 제어 큐빗 0와 타겟 큐빗 2에 추가
#GHZ 상태에 있는 큐빗
circ.cx(0, 2)

circ.draw('mpl')

#상태 벡터 백엔드
backend = Aer.get_backend('statevector_simulator')
job = backend.run(circ)
result = job.result()
#객체는 데이터를 가지고 있으며, 
# Qiskit 은 양자 회로에 대한 상태 벡터를 돌려주는 
# result.get_statevector(circ) 메소드를 제공한다.
outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)

#유니터리 벡엔드
# Run the quantum circuit on a unitary simulator backend
backend = Aer.get_backend('unitary_simulator')
job = backend.run(circ)
result = job.result()

# Show the results
print(result.get_unitary(circ, decimals=3))

#OpenQASM 후위 처리 장치
# Create a Quantum Circuit
meas = QuantumCircuit(3, 3)
meas.barrier(range(3))
# map the quantum measurement to the classical bits
meas.measure(range(3), range(3))

# The Qiskit circuit object supports composition using
# the compose method.
circ.add_register(meas.cregs[0])
qc = circ.compose(meas)

#drawing the circuit
qc.draw()

#결과와 히스토그램
# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = backend_sim.run(transpile(qc, backend_sim), shots=1024)

# Grab the results from the job.
result_sim = job_sim.result()

counts = result_sim.get_counts(qc)
print(counts)

plot_histogram(counts)