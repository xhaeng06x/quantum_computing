from qiskit import *
from qiskit.visualization import plot_histogram

# quantum circuit to make a Bell state
bell = QuantumCircuit(2, 2)
bell.h(0)
bell.cx(0, 1)

#측정하기
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
plot_histogram([counts, second_counts], legend=legend, figsize=(15,12), color=['pink', 'blue'], bar_labels=False)#figsize :그래프 사이즈 설정
