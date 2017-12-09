mport math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Ref. Torrejon, Tunable inertia of chiral magnetic domain walls
## y[0] is q (DW position), y[1] is psi (angle of moment in DW), y[2] is chi (angle of DW).
def one_dim_model_3var(y, t, Alpha, Gamma, Delta, Width, DWtype, H_K, H_DM, H_SH, K_eff, M_s):
	return \
	np.array([\
	(-Gamma * H_K * sin(2 * (y[1] - y[2])) / 2 + DWtype * math.pi * Gamma * H_DM * sin(y[1] - y[2]) / 2 + Alpha * Gamma * H_PIN(y[0]) + Alpha * DWtype * math.pi * Gamma * H_SH * cos(y[1]) / 2) * Delta / (cos(y[2]) * (1 + Alpha ** 2)),\
	(Alpha * Gamma * H_K * sin(2 * (y[1] - y[2])) / 2 - Alpha * math.pi * DWtype * Gamma * H_DM * sin(y[1] - y[2]) / 2 + Gamma * H_PIN(y[0]) + DWtype * math.pi * Gamma * H_SH * cos(y[1]) / 2) / (1 + Alpha ** 2),\
	(-H_K * sin(2 * (y[1] - y[2])) / 2 + DWtype * math.pi * H_DM * sin(y[1] - y[2]) / 2 - 2 * K_eff * tan(y[2]) / M_s + DWtype * math.pi * H_DM * cos(y[1] - y[2]) * tan(y[2]) / 2 - H_K * cos(y[1] - y[2])**2 * tan(y[2])) * 12 * Gamma / (Alpha * math.pi**2 * (tan(y[2])**2 + (Width / (math.pi * Delta * cos(y[2])))**2))\
	])

def H_K(T_FM, M_s, Delta):
	return Mu_0 * 4 * T_FM * M_S * log(2) / Delta

def H_DM(D, DWtype, Delta, M_s):
	return Mu_0 * D * DWtype / (Delta * M_s)

def H_SH(Theta_SH, Current, M_s, T_FM):
	return -Mu_0 * Hbar * Theta_SH * Current / (2 * Charge * M_s * T_FM)

def H_PIN(q):
	return 0

## Physical constants
Hbar = 1.0545718e-34	# Dirac constant. J*s.
Charge = 1.60217662e-19	# elementary charge. Unit:C.
Gamma = 1.7608598e11	# gyromagnetic ratio. rad/sT
Mu_0 = 4 * math.pi * 1e-07	# magnetic permiability. H/m.


## Consider X Ta / 1 W / 1 CoFeB / 2 MgO / 1 Ta, X = 2.5.
K_eff = 3.2e+05
M_s = 1.1e+06	# saturation magnetization. J/T.
Alpha = 0.05	# damping coefficient
DWtype = 1	# this means up/down DW. -1 if down/up DW.
Exchange = 1.5e-11
Delta = math.sqrt(K_eff / A)	# width of DW.
Width = 5.0e-06	# width of wire. 5um.
T_FM = 1.0e-09	# thickness of CoFeB. 1nm.
D = 0.24e-03	# DMI constant. J/m^2
Theta_SH = -0.21	# spin Hall angle.
Voltage = 25 # voltage. 25V.
#Rho_W = # resistivity of W. Ohm*m.
#Rho_Ta = # resistivity of Ta.
T_W = 1.0e-09	# thickness of W. 1nm.
T_Ta = 0.0e-09	# thickness of Ta. 0nm.
Length = 30e-06	# length of wire
#Current =
Current = 0.5e+12	# current density in heavy metal layer Ta / W. A/m^2.

T_max = 100e-09	# final time. 100ns.
T_div = 10	# the number of time step
t = np.linspace(0, T_max, T_div)	# time array when solutions are obtained.

# initial condition
y_0 = np.array([0.0, 0.0, 0.0])

y = odeint(one_dim_model_3var, y_0, t, args = (Alpha, Gamma, Delta, Width, DWtype, H_K(T_FM, M_s, Delta), H_DM(D, DWtype, Delta, M_s), H_SH(Theta_SH, Current, M_s, T_FM), K_eff, M_s))

plt.scatter(t * 1e+09, y[0] * 1e+06)
plt.xlabel("Time [ns]")
plt.ylabel("DW position [$\mu$m]")
plt.grid(True)
plt.show()


