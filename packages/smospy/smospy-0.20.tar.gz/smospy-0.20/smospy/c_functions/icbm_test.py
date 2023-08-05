import numpy as np
from signal_c_lib import *

x=Py_C_signal_lib()
a=np.arange(5)

#a=np.ones(100)
y=np.array([a,a,a])
print(x.icbm(y))
