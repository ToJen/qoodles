# from pyquil import get_qc, Program
# qvm = get_qc('9q-qvm')
# qvm.run(Program())

# qvm.run(Program('X 0'))
from pyquil import get_qc, Program
from pyquil.gates import CNOT, H, MEASURE
 
qvm = get_qc('2q-qvm')
 
p = Program()
p += H(0)
p += CNOT(0, 1)
ro = p.declare('ro', 'BIT', 2)
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])
p.wrap_in_numshots_loop(10)
 
qvm.run(p).tolist()