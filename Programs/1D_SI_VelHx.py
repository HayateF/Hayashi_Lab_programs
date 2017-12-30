####### Ref. Martinez, Coupled Dzyaloshinskii walls and their current-induced dynamics by the spin Hall effect
####### Ref. Torrejon, Tunable inertia of chiral magnetic domain walls
from math import *	# You don't have to add "math" before any modules of math. 
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## Ref. Martinez, Current-driven dynamics of Dzyaloshinskii domain walls in the presence of in-plane field
## y[0] is q (DW position), y[1] is phi (angle of moment in DW), y[2] is chi (angle of DW).
def one_dim_model_3var(y, t_0, H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, width, Q,  K_u, M_s, A, D, t_FM, b_J, xi):
	return \
	np.array([\
	(Delta / (cos(y[2]) * (1 + alpha**2))) \
		* ( Omega_A(y[1], y[2], H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J) \
			+ alpha * Omega_B(y[1], y[2], H_z, H_SH, H_R, 0, 0, Q, Delta, b_J, xi) ), \
	\
	(1 / (1 + alpha**2)) \
		* ( - alpha * Omega_A(y[1], y[2], H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J) \
			+ Omega_B(y[1], y[2], H_z, H_SH, H_R, 0, 0, Q, Delta, b_J, xi) ), \
	\
	(6 * gamma / ((alpha * mu_0 * M_s * Delta * pi**2) * (tan(y[2])**2 + (width / (pi * Delta * cos(y[2])))**2))) \
		* ( - sigma(y[1], y[2], H_x, H_y, H_K, H_R, Q, Delta, D, M_s, K_u, A) * sin(y[2]) \
			+ pi * D * Q * sin(y[1] - y[2]) \
			- mu_0 * H_K * M_s * Delta * sin(2 * (y[1] - y[2])) ) \
	])

def H_K(t_FM, M_s, Delta):	# anisotropy field
	return t_FM * M_s * log(2) / (pi * Delta)

def H_D(D, Delta, M_s):	# DM field
	return D / (mu_0 * Delta * M_s)

def H_SH(theta_SH, current, M_s, t_FM):	# field generated by spin current
	return - hbar * theta_SH * current / (2 * mu_0 * charge * M_s * t_FM)

def H_R(alpha_R, P, current, M_s):
	# alpha_R is Rashba parameter, P is spin polarization factor.
	#return alpha_R * P * current / (mu_0 + mu_B * M_s)
	return 0

def H_PIN(q, M_s, width, t_FM, V_0, period):	# pinning field
	# Ref. Martinez, Coupled Dzyaloshinkii walls and their current-induced dynamics by the spin Hall effect
	# H_pin = - (1 / 2 Mu_0 M_s L_y L_z) dV_pin / dx
	# L_y = width, L_z = t_FM, V_pin is a pinning potential.
	# Here I use V_pin (x) = V_0 sin(pi x / p)^2,
	# V_0 = 20 * 10^(-21) J = 20 * 10^(-14) erg, p = 21nm = 21 * 10^(-7) cm.
	# So in the cgs unit, H_pin = - (pi V_0 / p M_s width t_FM) sin(pi x / p) cos(pi x / p)
	return 0
	#return - (pi * V_0 / (period * M_s * width * t_FM)) * sin(pi * q / period) * cos (pi * q / period)

def H_th(alpha, temperature, M_s, Delta, t_FM, width):	# thermal field
	#return np.random.normal(0, sqrt(2 * alpha * k_B * temperature / (gamma * M_s * Delta * width * t_FM)))	
	return 0

def D(current):	# DMI constant depending on spin current. J/m^2.
	#return 0.24 + current * 1e-09
	return 0.24e-03

def b_J(current, P, M_s):	# STT coefficient
	#return - current * mu_B * P / (charge * M_s)
	return 0

def Omega_A(phi, chi, H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J):	
	return - (1/2) * gamma * H_K * sin(2 * (phi - chi)) \
			 - (pi/2) * gamma * H_y * cos(phi) \
			 + (pi/2) * gamma * H_x * sin(phi) \
			 + (pi/2) * gamma * H_D * Q * sin(phi - chi) \
			 - (pi/2) * gamma * H_R * cos(phi) \
			 + (b_J / Delta) * cos(chi)

def Omega_B(phi, chi, H_z, H_SH, H_R, H_PIN, H_th, Q, Delta, b_J, xi):
	return gamma * Q * (H_z + H_PIN + H_th) \
			+ (pi/2) * gamma * Q * H_SH * cos(phi) \
			- xi * (pi/2) * gamma * H_R * cos(phi) \
			+ xi * (b_J / Delta) * cos(chi)
			
def sigma(phi, chi, H_x, H_y, H_K, H_R, Q, Delta, D, M_s, K_u, A):
	return (1 / cos(chi)) * ( 4 * sqrt(A * K_u) \
			- Q * pi * D * cos(phi - chi) \
			+ mu_0 * H_K * M_s * Delta * cos(2 * (phi - chi))**2 \
			- pi * mu_0 * M_s * Delta * H_R * sin(phi) \
			- pi * mu_0 * M_s * Delta * H_y * sin(phi) \
			- pi * mu_0 * M_s * Delta * H_x * cos(phi) )




print ("flag 10")

## Physical constants
hbar = 1.0545718e-34	# Dirac constant. J*s.
charge = 1.60217662e-19	# elementary charge. Unit:C.
gamma = 1.7608598e+11	# gyromagnetic ratio. rad/sT
#k_B = 1.380649e-23	# Boltzmann constant. J/K.
mu_0 = 4 * pi * 1e-07	# magnetic permiability. H/m.
mu_B = 927.40100e-26	# Bohr magneton. J/T.
gamma *= mu_0	# the definition in Martinez's paper.

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
#voltage = 25 # voltage. 25V.
#rho_W = # resistivity of W. Ohm*m.
#rho_Ta = # resistivity of Ta.
#t_W = 1.0e-09	# thickness of W. 1nm.
#t_Ta = 0.0e-09	# thickness of Ta. 0nm.
#length = 30e-06	# length of wire
#V_0 = 20e-14	# pinning amplitude. erg.
#period = 21e-09	# pinning periodicity. 21nm. 

## External Field. A/m. 1 Oe is 10^3/(4 pi) A/m.
#H_x = 0
H_y = 0
H_z = 0

#np.random.seed(seed)	# set seed for Mersenne twister

# current density in heavy metal layer Ta / W. A/m^2.
# This should be negative, for the convenience later.
current = - 0.5e+12	

H_x_start = -1000e+03 / (4 * pi)
H_x_end = 1000e+03 / (4 * pi)
H_x_step = 50e+03 / (4 * pi)
H_x_list = np.arange(H_x_start, H_x_end, H_x_step, dtype = np.float64)	# x-field. A/m.
velocity_eff_p_updown = np.zeros(H_x_list.size) 
velocity_eff_p_downup = np.zeros(H_x_list.size) 
velocity_eff_n_updown = np.zeros(H_x_list.size) 
velocity_eff_n_downup = np.zeros(H_x_list.size) 
#velocity_stat = np.zeros(H_x_list.size)
#print (Current)

## time array
duration = 100e-09	# current pulse duration. 100ns.
t_step = 1e-12	# time step when we get the results, not a time step of numerical calculation.
t_1 = np.arange(0, duration, t_step, dtype = np.float64)	# time array when solutions are obtained.
## after switch of the current
t_end = 300e-09	# final time. 300ns.
t_2 = np.arange(duration, t_end, t_step, dtype = np.float64)

print ("flag 20")


i = 0
for H_x in H_x_list:
	current *= -1
	######## positive current ########
	### up-down calculation
	# initial condition
	y_0 = np.array([0.0, 0.0, 0.0])
	print ("flag 30")
	## solve the equation
	y_1 = odeint(one_dim_model_3var, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, 1, K_u, M_s, A, D(current), t_FM, 0, 0))	

	print ("flag 40")
	y_0 = y_1[-1]	# the initial condition is the final state of the previous calculation.
	y_2 = odeint(one_dim_model_3var, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, 1, K_u, M_s, A, D(0), t_FM, 0, 0))
	
	print("flag 50")
	velocity_eff_p_updown[i] = (y_2[-1, 0] / duration)

	### down-up calculation
	y_0 = np.array([0.0, 0.0, 0.0])
	y_1 = odeint(one_dim_model_3var, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, -1, K_u, M_s, A, D(current), t_FM, 0, 0))	
	y_0 = y_1[-1]	# the initial condition is the final state of the previous calculation.
	y_2 = odeint(one_dim_model_3var, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, -1, K_u, M_s, A, D(0), t_FM, 0, 0))
	velocity_eff_p_downup[i] = (y_2[-1, 0] / duration)

	current *= -1
	######## negative current ########
	### up-down calculation
	y_0 = np.array([0.0, 0.0, 0.0])
	y_1 = odeint(one_dim_model_3var, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, 1, K_u, M_s, A, D(current), t_FM, 0, 0))	
	y_0 = y_1[-1]	# the initial condition is the final state of the previous calculation.
	y_2 = odeint(one_dim_model_3var, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, 1, K_u, M_s, A, D(0), t_FM, 0, 0))
	velocity_eff_n_updown[i] = (y_2[-1, 0] / duration)
	### down-up calculation
	y_0 = np.array([0.0, 0.0, 0.0])
	y_1 = odeint(one_dim_model_3var, y_0, t_1, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
				0, H_SH(theta_SH, current, M_s, t_FM), \
				alpha, Delta, width, -1, K_u, M_s, A, D(current), t_FM, 0, 0))	
	y_0 = y_1[-1]	# the initial condition is the final state of the previous calculation.
	y_2 = odeint(one_dim_model_3var, y_0, t_2, \
		args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
				0, 0, \
				alpha, Delta, width, -1, K_u, M_s, A, D(0), t_FM, 0, 0))
	velocity_eff_n_downup[i] = (y_2[-1, 0] / duration)

	print (i, "-th calculation finished.")
	i += 1

## plot velocity
plt.figure(1)
plt.scatter(H_x_list[:] * 1e-03 * 4 * pi, velocity_eff_p_updown[:], label = "+ up-down")
plt.scatter(H_x_list[:] * 1e-03 * 4 * pi, velocity_eff_p_downup[:], label = "+ down-up")
plt.scatter(H_x_list[:] * 1e-03 * 4 * pi, velocity_eff_n_updown[:], label = "- up-down")
plt.scatter(H_x_list[:] * 1e-03 * 4 * pi, velocity_eff_n_downup[:], label = "- down-up")
plt.xlabel("x Field [Oe]")
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
#y_1 = odeint(one_dim_model_3var, y_0, t_1, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(current), Delta, M_s), \
#			0, H_SH(theta_SH, current, M_s, t_FM), \
#			alpha, Delta, width, Q, K_u, M_s, A, D(current), t_FM, 0, 0))
#y_0 = y_1[-1]
##y_2 = odeint(one_dim_model_3var, y_0, t_2, \
##	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
##			H_R(alpha_R, P, 0, M_s), H_SH(theta_SH, 0, M_s, t_FM), \
##			alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, b_J(0, P, M_s), xi))
#y_2 = odeint(one_dim_model_3var, y_0, t_2, \
#	args = (H_x, H_y, H_z, H_K(t_FM, M_s, Delta), H_D(D(0), Delta, M_s), \
#			0, 0, \
#			alpha, Delta, width, Q, K_u, M_s, A, D(0), t_FM, 0, 0))

# combine the two results.
#t = np.r_[t_1, t_2]	# np.r_ combines two arrays in the row direction.
#y = np.r_[y_1, y_2]
#v = np.gradient((y[:, 0] / t_step).flatten())
# np.flatten() returns a one-dimenstional array by flattening the input array.
# np.gradient calculates derivatives.
# np.gradient(y) means dy, and (t_end_1 / t_div_1) means dt. Then, v = dy/dt.
#print (v)

## plot position
#plt.figure(4)
#plt.scatter(t * 1e+09, y[:, 0] * 1e+06)
#plt.xlabel("Time [ns]")
#plt.ylabel("Position [$\mu$m]")
#plt.grid(True)

## plot velocity
#plt.figure(1)
#plt.scatter(t * 1e+09, v[:])
#plt.xlabel("Time [ns]")
#plt.ylabel("Velocity [m/s]")
#plt.grid(True)

## plot moment angle
#plt.figure(2)
#plt.scatter(t * 1e+09, y[:, 1] * 180 / pi)
#plt.grid(True)
#plt.xlabel("Time [ns]")
#plt.ylabel("Moment angle [degree]")

## plot DW angle
#plt.figure(3)
#plt.scatter(t * 1e+09, y[:, 2] * 180 / pi)
#plt.xlabel("Time [ns]")
#plt.ylabel("DW angle [degree]")
#plt.grid(True)

#plt.show()


