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
K_eff = 6.2e+05
M_s = 1100e+03	# saturation magnetization. J/Tm^3.
K_u = K_eff + mu_0 * M_s**2 / 2	# magnetic anisotropy energy.
#alpha = 0.01	# damping coefficient
alpha = 0.09
Q = 1	# this means up/down DW. -1 if down/up DW.
A = 1.5e-11	# exchange stiffness. J/m.
Delta = sqrt(A / K_eff)	# width of DW.
width = 5.0e-06	# width of wire. 5um.
t_FM = 1.0e-09	# thickness of CoFeB. 1nm.
#D_0 = 0.24e-03	# DMI constant. J/m^2
D_0 = 0.32e-03
theta_SH = -0.20	# spin Hall angle.
#theta_SH = 0.0
P = 0.72	# spin polarization factor
#xi = 0.09	# dimensionless non-adiabatic parameter
#xi = 0.01
xi = 0.0
alpha_R = -1.0e-10 * charge	# Rashba parameter. 1.0e-10 eV m is the typical value.
#C_1 = 3.0e-06	# DW-motion-to-DMI conversion coefficient
C_1 = 0.0
#C_2 = 1.0e-16
C_2 = 0.0
#voltage = 25 # voltage. 25V.
#rho_W = # resistivity of W. Ohm*m.
#rho_Ta = # resistivity of Ta.
#t_W = 1.0e-09	# thickness of W. 1nm.
#t_Ta = 0.0e-09	# thickness of Ta. 0nm.
#length = 30e-06	# length of wire
#V_0 = 20e-14	# pinning amplitude. erg.
#period = 21e-09	# pinning periodicity. 21nm. 

## External Field. A/m. 1 Oe is 10^3/(4 pi) A/m.
#H_x = -500 * 1e+03 / (4 * pi)
H_x = 0
#H_y = 1000 * 1e+03 / (4 * pi)
H_y = 0
#H_z = 100 * 1e+03 / (4 * pi)
H_z = 0

#np.random.seed(seed)	# set seed for Mersenne twister

#current = 0.5e+12	# current density in heavy metal layer Ta / W. A/m^2.
#current = 0.4e+12
current = 0

#current_start = -0.2e+08
#current_end = 0.2e+08
#current_step = 0.001e+08
#Current = np.arange(Current_start, Current_end, Current_step, dtype = np.float64)	# current density in heavy metal layer Ta / W. A/cm^2.

#velocity_stat = np.zeros(Current.size)
#print (Current)

## time array
#duration = 100e-09	# current pulse duration. 10ns.
duration = 2.6e-09
t_step = 1e-12	# time step when we get the results, not a time step of numerical calculation.
t_1 = np.arange(0, duration, t_step, dtype = np.float64)	# time array when solutions are obtained.
## after switch of the current
t_end = 300e-09	# final time. 300ns.
t_2 = np.arange(duration, t_end, t_step, dtype = np.float64)

print ("flag 20")

bJ = 0
#bJ = b_J(current, P, M_s)

HR = 0
#HR = H_R(alpha_R, P, current, M_s)

#D_0 = 0.21e-03	# critical value
D_0 = 0.15e-03
if H_D(D(D_0, 0), Delta, M_s) * pi / 2 > H_K(t_FM, M_s, Delta):
	print ("phi is", 0)
else:
	print ("phi is", acos(H_D(D(D_0, 0), Delta, M_s) * pi / (2 * H_K(t_FM, M_s, Delta))))


#y_0 = np.array([0.0, - (Q-1) * pi / 2, 0.0])
y_0 = np.array([0.0, - (Q-1) * pi / 2 + 0.000001, 0.0])
#y_0 = np.array([0.0, pi, 0.0])
#y_1 = odeint(one_dim_model_3var, y_0, t_1, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
#			H_R(alpha_R, P, current, M_s), H_SH(theta_SH, current, M_s, t_FM), \
#			alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, b_J(current, P, M_s), xi))
y_1 = odeint(one_dim_model_3var_ex, y_0, t_1, \
	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(D_0, current), Delta, M_s), \
			HR, H_SH(theta_SH, current, M_s, t_FM), \
			alpha, Delta, width, Q, K_u, M_s, A, D(D_0, current), t_FM, bJ, xi, current, C_1, C_2))
y_0 = y_1[-1]
#y_2 = odeint(one_dim_model_3var, y_0, t_2, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
#			H_R(alpha_R, P, 0, M_s), H_SH(theta_SH, 0, M_s, t_FM), \
#			alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, b_J(0, P, M_s), xi))
y_2 = odeint(one_dim_model_3var_ex, y_0, t_2, \
	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(D_0, 0), Delta, M_s), \
			0, 0, \
			alpha, Delta, width, Q, K_u, M_s, A, D(D_0, 0), t_FM, 0, xi, 0, C_1, C_2))

# combine the two results.
t = np.r_[t_1, t_2]	# np.r_ combines two arrays in the row direction.
y = np.r_[y_1, y_2]
v = np.gradient((y[:, 0] / t_step).flatten())
# np.flatten() returns a one-dimenstional array by flattening the input array.
# np.gradient calculates derivatives.
# np.gradient(y) means dy, and (t_end_1 / t_div_1) means dt. Then, v = dy/dt.
#print (v)

print ("The effective velocity is", y_2[-1][0] / duration, ".")

## plot position
plt.figure(4)
plt.scatter(t * 1e+09, y[:, 0] * 1e+06)
plt.xlabel("Time [ns]")
plt.ylabel("Position [$\mu$m]")
plt.grid(True)

## plot velocity
plt.figure(1)
plt.scatter(t * 1e+09, v[:])
plt.xlabel("Time [ns]")
plt.ylabel("Velocity [m/s]")
plt.grid(True)

## plot moment angle
plt.figure(2)
plt.scatter(t * 1e+09, y[:, 1] * 180 / pi)
plt.grid(True)
plt.xlabel("Time [ns]")
plt.ylabel("Moment angle [degree]")

## plot DW angle
plt.figure(3)
plt.scatter(t * 1e+09, y[:, 2] * 180 / pi)
plt.xlabel("Time [ns]")
plt.ylabel("DW angle [degree]")
plt.grid(True)

plt.show()

#i = 0
#for J in Current:
#	# initial condition
#	y_0 = np.array([0.0, 0.0, 0.0])
#	print ("flag 30")
#	## solve the equation
#	y_1 = odeint(one_dim_model_3var, y_0, t_1, args = (Alpha, Gamma, Delta, Width, DWtype, H_K(T_FM, M_s, Delta), H_DM(D(J), DWtype, Delta, M_s), H_SH(Theta_SH, J, M_s, T_FM), K_eff, M_s, T_FM, V_0, Period))
#	
#	print ("flag 40")
#	y_0 = y_1[-1]	# the initial condition is the final state of the previous calculation.
#	y_2 = odeint(one_dim_model_3var, y_0, t_2, args = (Alpha, Gamma, Delta, Width, DWtype, H_K(T_FM, M_s, Delta), H_DM(D(0), DWtype, Delta, M_s), H_SH(Theta_SH, 0, M_s, T_FM), K_eff, M_s, T_FM, V_0, Period))
#	
#	print("flag 50")
#	velocity_eff[i] = (y_2[-1, 0] / Duration) * 1e-06	# 1e-06 is conversion of um/s into m/s
#	velocity_stat[i] = (y_1[-1, 0] / Duration) * 1e-06	
#	print (i, "-th calculation finished.")
#	i += 1
#
### plot velocity
#plt.figure(1)
#plt.scatter(Current[:], velocity_eff[:], label = "effective")
#plt.scatter(Current[:], velocity_stat[:], label = "stationary")
#plt.xlabel("Current density [A/cm$^2$]")
#plt.ylabel("Velocity [m/s]")
#plt.legend()
#plt.grid(True)
#
### plot velocity ratio
#ratio = velocity_eff / velocity_stat
#plt.figure(2)
#plt.scatter(Current[:], ratio[:], label = "velocity ratio")
#plt.xlabel("Current density [A/cm$^2$]")
#plt.ylabel("Velocity Ratio")
#plt.legend()
#plt.grid(True)
#
#plt.show()




