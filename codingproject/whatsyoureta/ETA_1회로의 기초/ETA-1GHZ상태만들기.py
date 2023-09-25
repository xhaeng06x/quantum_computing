import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram

#양자 큐빗 3개 생성
circ = QuantumCircuit(3)

#h게이트를 양자 큐빗 0에 추가
circ.h(0)
#CNOT 게이트를 제어 큐빗 0와 타겟 큐빗 1에 추가
#벨 상태에 있는 큐빗
circ.cx(0, 1)
#CNOT 게이트를 제어 큐빗 0와 타겟 큐빗 2에 추가
#GHZ 상태에 있는 큐빗
circ.cx(0, 2)

#회로 시각화 하기
circ.draw('mpl')

#회로 시뮬레이션
#시뮬 초깋화
state = Statevector.from_int(0, 2**3)
#퀀텀 서킷에 의해 시뮬의 상태를 전환한다. 
state = state.evolve(circ)

#draw using latex
state.draw('latex')

#state.draw('qsphere')

