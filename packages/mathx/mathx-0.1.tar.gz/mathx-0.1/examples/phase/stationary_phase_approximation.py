from scipy.special import airy
import numpy as np
from mathx import phase

##
##
# print(abs(intf_num),np.angle(intf_num),abs(intf_spa),np.angle(intf_spa))
# ##
#  print(abs(intf_num),np.angle(intf_num),abs(intf_spa),np.angle(intf_spa))
# cintf_num=np.cumsum(f)*(t[1]-t[0])
# pg.plot(t,abs(cintf_num))
##
g0 = 0
g1 = 1
S0 = 4
S1 = 5
S3 = 6
w = 0.5
t = np.linspace(-5, 5, 1e6)
S = S0 + S1*t + S3*t**3/6
f = (g0 + g1*t)*np.exp(1j*S - 0.5*(t/w)**2)
intf_num = np.trapz(f, t)
intf_spa = phase.approximate_phase_inflexion(g0, g1, S0, S1, S3)  # pg.plot(t,f.real)
