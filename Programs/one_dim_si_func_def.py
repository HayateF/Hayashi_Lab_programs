####### Ref. Martinez, Coupled Dzyaloshinskii walls and their current-induced dynamics by the spin Hall effect
####### Ref. Torrejon, Tunable inertia of chiral magnetic domain walls
from math import *	# You don't have to add "math" before any modules of math. 
import numpy as np

## Ref. Martinez, Current-driven dynamics of Dzyaloshinskii domain walls in the presence of in-plane field
## y[0] is q (DW position), y[1] is phi (angle of moment in DW), y[2] is chi (angle of DW).
def one_dim_model_3var_ex(y, t_0, H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, width, Q,  K_u, M_s, A, D, t_FM, b_J, xi, current, C_1, C_2):
	return \
	np.array([\
#	(Delta / (cos(y[2]) * (1 + alpha**2))) \
#		* ( Omega_A(y[1], y[2], H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J) \
#			+ alpha * Omega_B(y[1], y[2], H_z, H_SH, H_R, 0, 0, Q, Delta, b_J, xi) ), \
	q_dot(y[1], y[2], H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, Q, M_s, b_J, xi, current, C_1, C_2), \
	\
	(1 / (1 + alpha**2)) \
		* ( - alpha * Omega_A(y[1], y[2], H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J) \
			+ Omega_B(y[1], y[2], H_z, H_SH, H_R, 0, 0, Q, Delta, b_J, xi) \
			- alpha * (pi/2) * gamma * Q * (C_2 * current * sin(y[1]) * sin(y[1] - y[2]) / (mu_0 * M_s * Delta)) \
			- alpha * (pi/2) * gamma * Q * (C_1 * sin(y[1]) * sin(y[1] - y[2]) / (mu_0 * M_s * Delta)) \
				* q_dot(y[1], y[2], H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, Q, M_s, b_J, xi, current, C_1, C_2) ), \
	\
	(6 * gamma / ((alpha * mu_0 * M_s * Delta * pi**2) * (tan(y[2])**2 + (width / (pi * Delta * cos(y[2])))**2))) \
		* ( - sigma(y[1], y[2], H_x, H_y, H_K, H_R, Q, Delta, D, M_s, K_u, A) * sin(y[2]) \
			+ pi * D * Q * sin(y[1] - y[2]) \
			- mu_0 * H_K * M_s * Delta * sin(2 * (y[1] - y[2])) \
			+ pi * Q * sin(y[1] - y[2]) * C_2 * current * sin(y[1]) \
			+ tan(y[2]) * Q * pi * cos(y[1] - y[2]) * C_2 * current * sin(y[1]) \
			+ pi * Q * sin(y[1] - y[2]) * C_1 * sin(y[1]) \
				* q_dot(y[1], y[2], H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, Q, M_s, b_J, xi, current, C_1, C_2) \
			+ tan(y[2]) * Q * pi * cos(y[1] - y[2]) * C_1 * sin(y[1]) \
				* q_dot(y[1], y[2], H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, Q, M_s, b_J, xi, current, C_1, C_2) ) \
	])

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

def q_dot(phi, chi, H_x, H_y, H_z, H_K, H_D, H_R, H_SH, alpha, Delta, Q, M_s, b_J, xi, current, C_1, C_2):	# time derivative of q
	return 	(Delta / (cos(chi) * (1 + alpha**2 - (pi/2) * Q * gamma * (C_1 / (mu_0 * M_s)) * sin(phi) * sin(phi - chi) / cos(chi)))) \
				* ( Omega_A(phi, chi, H_x, H_y, H_K, H_D, H_R, Q, Delta, b_J) \
					+ alpha * Omega_B(phi, chi, H_z, H_SH, H_R, 0, 0, Q, Delta, b_J, xi) \
					+ (pi/2) * gamma * Q * sin(phi - chi) * (C_2 * current * sin(phi)) / (mu_0 * M_s * Delta) )

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

## Physical constants
hbar = 1.0545718e-34	# Dirac constant. J*s.
charge = 1.60217662e-19	# elementary charge. Unit:C.
gamma = 1.7608598e+11	# gyromagnetic ratio. rad/sT
#k_B = 1.380649e-23	# Boltzmann constant. J/K.
mu_0 = 4 * pi * 1e-07	# magnetic permiability. H/m.
mu_B = 927.40100e-26	# Bohr magneton. J/T.
gamma *= mu_0	# the definition in Martinez's paper.

