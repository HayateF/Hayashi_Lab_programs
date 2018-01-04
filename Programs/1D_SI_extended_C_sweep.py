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
K_eff = 3.2e+05	# effective magnetic anisotropy energy. J/m^3.
M_s = 1100e+03	# saturation magnetization. J/Tm^3.
K_u = K_eff + mu_0 * M_s**2 / 2	# magnetic anisotropy energy.
alpha = 0.01	# damping coefficient
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
C = 1.0e-09	# DW-motion-to-DMI conversion coefficient
#voltage = 25 # voltage. 25V.
#rho_W = # resistivity of W. Ohm*m.
#rho_Ta = # resistivity of Ta.
#t_W = 1.0e-09	# thickness of W. 1nm.
#t_Ta = 0.0e-09	# thickness of Ta. 0nm.
#length = 30e-06	# length of wire
#V_0 = 20e-14	# pinning amplitude. erg.
#period = 21e-09	# pinning periodicity. 21nm. 

## External Field. A/m. 1 Oe is 10^3/(4 pi) A/m.
H_x = 0
H_y = 0
H_z = 0

#np.random.seed(seed)	# set seed for Mersenne twister

current = 0.5e+12	# current density in heavy metal layer Ta / W. A/m^2.

C_i_start = -10	# C starts from 1e-10
C_i_end = -5	# C ends at 1e-05
C_i_split = 100
C_list = np.logspace(C_i_start, C_i_end, C_i_split)
print (C_list) 
velocity_eff = np.zeros(C_list.size) 
#velocity_stat = np.zeros(Current.size)

## time array
duration = 100e-09	# current pulse duration. 100ns.
t_step = 1e-12	# time step when we get the results, not a time step of numerical calculation.
t_1 = np.arange(0, duration, t_step, dtype = np.float64)	# time array when solutions are obtained.
## after switch of the current
t_end = 300e-09	# final time. 300ns.
t_2 = np.arange(duration, t_end, t_step, dtype = np.float64)

print ("flag 20")


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


i = 0
for C in C_list:
	y_0 = np.array([0.0, 0.0, 0.0])
	y_1 = odeint(one_dim_model_3var_ex, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, 0, 0, C))
	y_0 = y_1[-1]
	y_2 = odeint(one_dim_model_3var_ex, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, 0, 0, C))
	
	velocity_eff[i] = (y_2[-1, 0] / duration)
	print (i, "-th calculation finished.")
	i += 1

## plot velocity
plt.figure(1)
plt.scatter(C_list[:] * 1e+03, velocity_eff[:], label = "effective")
plt.xscale("log")
plt.xlim([1e-08, 1e-01])
plt.xlabel("Conversion Coefficient [mJ/m$^2$ / (m/s)]")
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




