from qiskit import *
from qiskit.visualization import plot_bloch_multivector, plot_bloch_vector

# quantum circuit to make a Bell state
bell = QuantumCircuit(2, 2)
bell.h(0)
bell.cx(0, 1)

meas = QuantumCircuit(2, 2)
meas.measure([0,1], [0,1])

# execute the quantum circuit
backend = BasicAer.get_backend('qasm_simulator') # the device to run on
circ = bell.compose(meas)
result = backend.run(transpile(circ, backend), shots=1000).result()
counts  = result.get_counts(circ)
print(counts)

backend = BasicAer.get_backend('statevector_simulator') # the device to run on
result = backend.run(transpile(bell, backend)).result()
psi  = result.get_statevector(bell)

plot_bloch_multivector(psi)

#양자 시스템을 그리는 표준적인 방법은 블로흐 (Bloch) 벡터를 사용하는 것이다. 
#이는 하나의 큐비트에 대해서만 동작하고, 블로흐 벡터를 입력으로 받는다.

plot_bloch_vector([0,1,0], title='My Bloch Sphere')