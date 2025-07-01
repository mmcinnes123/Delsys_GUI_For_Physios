import numpy as np
import qmt
np.set_printoptions(suppress=True)

a1, b1, c1 = 1, 0, 0
a2, b2, c2 = 0, 1, 0
a3, b3, c3 = 0, 0, 1



# TODO: Get humerus and forearm trans quats then do joint calculations.
# Should be easier to implement different calibrations from there

# Transformation matrics to transform sensor local frames to match ISB body frames
thorax_trans_quat = qmt.quatFromRotMat([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
humerus_trans_quat = qmt.quatFromRotMat([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
forearm_trans_quat = qmt.quatFromRotMat([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])

sensor_t_ori =  qmt.quatFromRotMat([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
output = qmt.qmult(sensor_t_ori, thorax_trans_quat)
# print(qmt.quatToRotMat(output))