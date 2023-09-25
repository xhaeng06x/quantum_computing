from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere

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

#히스토그램
plot_histogram(counts)

#히스토그램 그래프 옵션 
# Execute 2-qubit Bell state again
second_result = backend.run(transpile(circ, backend), shots=1000).result()#트랜스파일: 서킷(cric)을 벡엔드로 소스코드를 변환한다.
second_counts  = second_result.get_counts(circ)
# Plot results with legend
legend = ['First execution', 'Second execution']#히스토그램에 레이블 지정
plot_histogram([counts, second_counts], legend=legend, figsize=(15,12), color=['red', 'blue'], bar_labels=False)#figsize :그래프 사이즈 설정

#마치 건물처럼 표현하는 그래프
backend = BasicAer.get_backend('statevector_simulator') # the device to run on
result = backend.run(transpile(bell, backend)).result()
psi  = result.get_statevector(bell)

plot_state_city(psi)


#힌튼 
plot_state_hinton(psi)

#qsphere 상태 벡터의 진폭과 위상이 구체에 그려지는 양자 상태
plot_state_qsphere(psi)

#블로흐 구면 
plot_bloch_multivector(psi)