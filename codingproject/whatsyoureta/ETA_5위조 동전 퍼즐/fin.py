import numpy as np
from numpy import pi
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, BasicAer, execute, Aer
from collections import Counter
from qiskit.visualization import plot_histogram
from qiskit import *

qreg_q = QuantumRegister(10, 'q')
creg_c = ClassicalRegister(10, 'c')
qc = QuantumCircuit(qreg_q, creg_c)

N = 9
for i in range(N):
    qc.h(i)

for i in range(N):
    qc.cx(i ,9)

qc.measure(9, 8)
qc.x(qreg_q[9]).c_if(creg_c, 0)
qc.h(qreg_q[9]).c_if(creg_c, 0)

for i in range(N):
    qc.h(qreg_q[i]).c_if(creg_c, 256)

#원하는 중첩 상태의 양자 저울을 적용한다.
#qc.cx(qreg_q[k]).c_if(creg_c, 0)
k=5#위조 동전의 개수
qc.cx(qreg_q[k], qreg_q[N]).c_if(creg_c, 0)

for i in range(N):
    qc.h(qreg_q[i]).c_if(creg_c, 256)

#qc.measure(0,0)
for i in range(9):
    qc.measure(qreg_q[i],creg_c[i])


backend_sim = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator.
# We've set the number of repeats of the circuit
# to be 1024, which is the default.
job_sim = backend_sim.run(transpile(qc, backend_sim), shots=1)

# Grab the results from the job.
result_sim = job_sim.result()

answer = result_sim.get_counts()
print(answer)

for key in answer.keys():
    normalFlag,_ = Counter(key[1:]).most_common(1)[0]

for i in range(2, len(key)):
    if key[i] != normalFlag:
        print("위조 동전은 ", len(key)-i)
        break
        
qc.draw('mpl')
