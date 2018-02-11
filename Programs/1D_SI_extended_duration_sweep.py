####### Ref. Martinez, Coupled Dzyaloshinskii walls and their current-induced dynamics by the spin Hall effect
####### Ref. Torrejon, Tunable inertia of chiral magnetic domain walls
from math import *	# You don't have to add "math" before any modules of math. 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from one_dim_si_func_def import *

## Ref. Martinez, Current-driven dynamics of Dzyaloshinskii domain walls in the presence of in-plane field
## y[0] is q (DW position), y[1] is phi (angle of moment in DW), y[2] is chi (angle of DW).

#temperature = 300	# ambient temperature
#seed = 213	# seed of Mersenne twister

## Consider W / 1 CoFeB / 2 MgO / 1 Ta.
#K_eff = 3.2e+05	# effective magnetic anisotropy energy. J/m^3.
K_eff = 6.2e+05	# effective magnetic anisotropy energy. for E152-07 2C. J/m^3.
M_s = 1100e+03	# saturation magnetization. J/Tm^3.
K_u = K_eff + mu_0 * M_s**2 / 2	# magnetic anisotropy energy.
#alpha = 0.01	# damping coefficient
alpha = 0.05
Q = 1	# this means up/down DW. -1 if down/up DW.
A = 1.5e-11	# exchange stiffness. J/m.
Delta = sqrt(A / K_eff)	# width of DW.
width = 5.0e-06	# width of wire. 5um.
t_FM = 1.0e-09	# thickness of CoFeB. 1nm.
#D = 0.24e-03	# DMI constant. J/m^2
theta_SH = -0.21	# spin Hall angle.
#P = 0.72	# spin polarization factor
#xi = 0	# dimensionless non-adiabatic parameter
#alpha_R = 0	# Rashba parameter
#C_1 = 1.0e-09	# DW-motion-to-DMI conversion coefficient
C_1 = 0.0
C_2 = 0.0
#voltage = 25 # voltage. 25V.
#rho_W = 120e-08	# resistivity of W. Ohm*m.
#rho_Ta = 200e-08	# resistivity of Ta.
#t_W = 1.0e-09	# thickness of W. 1nm.
#t_Ta = 2.3e-09	# thickness of Ta. 0nm.
#length = 30e-06	# length of wire
#V_0 = 20e-14	# pinning amplitude. erg.
#period = 21e-09	# pinning periodicity. 21nm. 

## External Field. A/m. 1 Oe is 10^3/(4 pi) A/m.
H_x = 0
H_y = 0
H_z = 0

#np.random.seed(seed)	# set seed for Mersenne twister

current = 0.5e+12	# current density in heavy metal layer Ta / W. A/m^2.

pulse_start = 1	# pulse duration starts from 1ns
pulse_end = 100	# pulse duration ends at 100ns
pulse_step = 1
pulse_list = np.arange(pulse_start, pulse_end, pulse_step, dtype = np.float64)
velocity_eff = np.zeros(pulse_list..size) 
#velocity_stat = np.zeros(Current.size)


t_step = 1e-11	# time step when we get the results, not a time step of numerical calculation.
t_end = 300e-09	# final time. 300ns.


i = 0
for duration in pulse_list:
	## time array
	t_1 = np.arange(0, duration * 1e-09, t_step, dtype = np.float64)	# time array when solutions are obtained.
	t_2 = np.arange(duration * 1e-09, t_end, t_step, dtype = np.float64)

	y_0 = np.array([0.0, 0.0, 0.0])
	y_1 = odeint(one_dim_model_3var_ex, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, 0, 0, current, C_1, C_2))
	y_0 = y_1[-1]
	y_2 = odeint(one_dim_model_3var_ex, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, 0, 0, current, C_1, C_2))
	
	velocity_eff[i] = (y_2[-1, 0] / duration * 1e+09)
	print (i, "-th calculation finished.")
	i += 1

## plot velocity
plt.figure(1)
plt.scatter(pulse_list[:], velocity_eff[:], label = "effective")
plt.xlabel("Pulse width [ns]")
plt.ylabel("Velocity [m/s]")
plt.legend()
plt.grid(True)

## plot velocity ratio
#ratio = velocity_eff / velocity_stat
#plt.figure(2)
#plt.scatter(Current[:], ratio[:], label = "velocity ratio")
#plt.xlabel("Current density [A/cm$^2$]")
#plt.ylabel("Velocity Ratio")
#plt.legend()
#plt.grid(True)

plt.show()


#y_0 = np.array([0.0, 0.0, 0.0])
##y_1 = odeint(one_dim_model_3var, y_0, t_1, \
##	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
##			H_R(alpha_R, P, current, M_s), H_SH(theta_SH, current, M_s, t_FM), \
##			alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, b_J(current, P, M_s), xi))
#y_1 = odeint(one_dim_model_3var_ex, y_0, t_1, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
#			0, H_SH(theta_SH, current, M_s, t_FM), \
#			alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, 0, 0, C))
#y_0 = y_1[-1]
##y_2 = odeint(one_dim_model_3var, y_0, t_2, \
##	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
##			H_R(alpha_R, P, 0, M_s), H_SH(theta_SH, 0, M_s, t_FM), \
##			alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, b_J(0, P, M_s), xi))
#y_2 = odeint(one_dim_model_3var_ex, y_0, t_2, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
#			0, 0, \
#			alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, 0, 0, C))
#
## combine the two results.
#t = np.r_[t_1, t_2]	# np.r_ combines two arrays in the row direction.
#y = np.r_[y_1, y_2]
#v = np.gradient((y[:, 0] / t_step).flatten())
## np.flatten() returns a one-dimenstional array by flattening the input array.
## np.gradient calculates derivatives.
## np.gradient(y) means dy, and (t_end_1 / t_div_1) means dt. Then, v = dy/dt.
##print (v)
#
### plot position
#plt.figure(4)
#plt.scatter(t * 1e+09, y[:, 0] * 1e+06)
#plt.xlabel("Time [ns]")
#plt.ylabel("Position [$\mu$m]")
#plt.grid(True)
#
### plot velocity
#plt.figure(1)
#plt.scatter(t * 1e+09, v[:])
#plt.xlabel("Time [ns]")
#plt.ylabel("Velocity [m/s]")
#plt.grid(True)
#
### plot moment angle
#plt.figure(2)
#plt.scatter(t * 1e+09, y[:, 1] * 180 / pi)
#plt.grid(True)
#plt.xlabel("Time [ns]")
#plt.ylabel("Moment angle [degree]")
#
### plot DW angle
#plt.figure(3)
#plt.scatter(t * 1e+09, y[:, 2] * 180 / pi)
#plt.xlabel("Time [ns]")
#plt.ylabel("DW angle [degree]")
#plt.grid(True)
#
#plt.show()


