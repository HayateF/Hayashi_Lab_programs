from math import *	# You don't have to add "math" before any modules of 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Ref. Torrejon, Tunable inertia of chiral magnetic domain walls
## y[0] is q (DW position), y[1] is psi (angle of moment in DW), y[2] is chi (angle of DW).
def one_dim_model_3var(y, t, Alpha, Gamma, Delta, Width, DWtype, H_K, H_DM, H_SH, K_eff, M_s):
	return \
	np.array([\
	1e+04 * (-Gamma * H_K * sin(2 * (y[1] - y[2])) / 2 + DWtype * pi * Gamma * H_DM * sin(y[1] - y[2]) / 2 + Alpha * Gamma * H_PIN(y[0]) + Alpha * DWtype * pi * Gamma * H_SH * cos(y[1]) / 2) * Delta / (cos(y[2]) * (1 + Alpha ** 2)),\
	(Alpha * Gamma * H_K * sin(2 * (y[1] - y[2])) / 2 - Alpha * pi * DWtype * Gamma * H_DM * sin(y[1] - y[2]) / 2 + Gamma * H_PIN(y[0]) + DWtype * pi * Gamma * H_SH * cos(y[1]) / 2) / (1 + Alpha ** 2),\
	(- H_K * sin(2 * (y[1] - y[2])) / 2 + DWtype * pi * H_DM * sin(y[1] - y[2]) / 2 - 2 * K_eff * tan(y[2]) / M_s + DWtype * pi * H_DM * cos(y[1] - y[2]) * tan(y[2]) / 2 - H_K * cos(y[1] - y[2])**2 * tan(y[2])) * 12 * Gamma / (Alpha * pi**2 * (tan(y[2])**2 + (Width / (pi * Delta * cos(y[2])))**2))\
	])

def H_K(T_FM, M_s, Delta):
	return 4 * T_FM * M_s * log(2) / Delta

def H_DM(D, DWtype, Delta, M_s):
	return D * DWtype / (Delta * M_s)

def H_SH(Theta_SH, Current, M_s, T_FM):
	return - Hbar * Theta_SH * Current / (2 * Charge * M_s * T_FM)

def H_PIN(q):
	return 0

## Physical constants
Hbar = 1.0545718e-27	# Dirac constant. erg*s.
Charge = 1.60217662e-19	# elementary charge. Unit:C.
Gamma = 1.7608598e+7	# gyromagnetic ratio. rad/sG
#Mu_0 = 4 * pi * 1e-07	# magnetic permiability. H/m.


## Consider X Ta / 1 W / 1 CoFeB / 2 MgO / 1 Ta, X = 2.5.
K_eff = 3.2e+06	# effective magnetic anisotropy enery. erg/cm^3.
M_s = 1100	# saturation magnetization. emu/cm^3.
Alpha = 0.01	# damping coefficient
DWtype = 1	# this means up/down DW. -1 if down/up DW.
Exchange = 1.5e-06	# exchange stiffness. erg/cm.
Delta = sqrt(Exchange / K_eff)	# width of DW.
Width = 5.0e-04	# width of wire. 5um.
T_FM = 1.0e-07	# thickness of CoFeB. 1nm.
D = 0.24	# DMI constant. erg/cm^2
Theta_SH = 0.21	# spin Hall angle.
Voltage = 25 # voltage. 25V.
#Rho_W = # resistivity of W. Ohm*m.
#Rho_Ta = # resistivity of Ta.
#T_W = 1.0e-07	# thickness of W. 1nm.
#T_Ta = 0.0e-07	# thickness of Ta. 0nm.
#Length = 30e-04	# length of wire
#Current =
Current = 0.5e+8	# current density in heavy metal layer Ta / W. A/cm^2.

T_max = 100e-09	# final time. 100ns.
T_div = 10000	# the number of time step
t = np.linspace(0, T_max, T_div)	# time array when solutions are obtained.

# initial condition
y_0 = np.array([0.0, 0.0, 0.0])

y = odeint(one_dim_model_3var, y_0, t, args = (Alpha, Gamma, Delta, Width, DWtype, H_K(T_FM, M_s, Delta), H_DM(D, DWtype, Delta, M_s), H_SH(Theta_SH, Current, M_s, T_FM), K_eff, M_s))

#plt.scatter(t * 1e+09, y[:, 0] * 1e+06)
plt.scatter(t * 1e+09, y[:, 0])
plt.xlabel("Time [ns]")
plt.ylabel("DW position [$\mu$m]")
plt.grid(True)
plt.show()

plt.scatter(t * 1e+09, y[:, 1])
plt.show()

plt.scatter(t * 1e+09, y[:, 2])
plt.show()




