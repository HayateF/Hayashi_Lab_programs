from operator import itemgetter
import numpy as np
import math	# for sqrt function
readfilename = "velocity_v1_51a_20170825.dat"
writefilename = "velocity_averaged_by_pulse_length_28V.dat"


# return real pulse width from the set value
# fitting results are
# REAL_WIDTH = a * SET_WIDTH + b,
# a = 1.00333 \pm 0.0009972,
# b = -0.953443 \pm 0.03989
# But here, too short pulse length leads to incorrect pulse length.
# So, this function just returns the set pulse length.
def pulse_width(w):
	#return 1.003 * w - 0.95
	return w


#################################################
########### main starts from here ###############
#################################################

data = np.loadtxt(readfilename, delimiter = "\t", usecols = (9, 11, 14, 0, 1), skiprows = 1)
#data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", usecols = (8, 9, 11, 14), skiprows = 1)
# \t means tab
# column 9 is Pulse_Amp, column 10 is Pulse length, column 12 is Slope1, column 15 is Slope2,
# but you have to note that the number starts from 0.
# Column 0 and 1 will be used to store the standard errors.

# You have to sort an input file by pulse length in ascending order.
# But if you sort with np.sort directly, you will sort all columns independently.
data = sorted(data, key = itemgetter(0))
print ("sorted data is\n", data)

# itemgetter(8, 9) means sort by column 8 which is followed by sort by column 9.

# data = np.sort(data, axis = 0)	# axis = 0 means sort by column. axis = 1 means sort by row.
# np.sort does not suit this time because np.sort will sorts all columns independently.


current_row = 0
using_row = 0	# the row in which we will store data next
n_row = 1	# the number of rows whose pulse lengths are the same
v_u = 0.0	# "u" means "up-down" 
v_d = 0.0	# "d" means "down-up"
stderr_u = 0.0
stderr_d = 0.0
# We calculate standard error by the formula
# stderr = \sqrt[(\sum x^2 - n m^2) / (n-1)]
# where x is a sample value, m is the average of the sample values, and n is the number of the samples.

while current_row < len(data):
	if current_row == (len(data) - 1):
		v_u = (v_u + data[current_row][1] ) / n_row	# calculated average
		v_d = (v_d + data[current_row][2] ) / n_row
		stderr_u = math.sqrt((stderr_u + data[current_row][1] ** 2 - n_row * v_u ** 2) / (n_row - 1))
		stderr_d = math.sqrt((stderr_d + data[current_row][2] ** 2 - n_row * v_d ** 2) / (n_row - 1))
		data[using_row][0] = pulse_width(data[current_row][0])
		data[using_row][1] = v_u
		data[using_row][2] = v_d
		data[using_row][3] = stderr_u
		data[using_row][4] = stderr_d

		using_row += 1
	elif (data[current_row + 1][0] - data[current_row][0]) > 0.1:
		v_u = (v_u + data[current_row][1] ) / n_row	# calculated average
		v_d = (v_d + data[current_row][2] ) / n_row
		stderr_u = math.sqrt((stderr_u + data[current_row][1] ** 2 - n_row * v_u ** 2) / (n_row - 1))
		stderr_d = math.sqrt((stderr_d + data[current_row][2] ** 2 - n_row * v_d ** 2) / (n_row - 1))
		data[using_row][0] = pulse_width(data[current_row][0])
		data[using_row][1] = v_u
		data[using_row][2] = v_d
		data[using_row][3] = stderr_u
		data[using_row][4] = stderr_d

		using_row += 1
		n_row = 1
		v_u = 0.0
		v_d = 0.0
		stderr_u = 0.0
		stderr_d = 0.0
	else:
		v_u += data[current_row][1]
		v_d += data[current_row][2]
		# These sumation above lead to average later.
		stderr_u += data[current_row][1] ** 2
		stderr_d += data[current_row][2] ** 2
		n_row += 1

	current_row += 1


# Delete list elements list[i] to list[j-1] by "del list[i: j]".
del data[using_row: len(data)]
# Columns are "Pulse length [ns]", "Slope1 [m/s]", "Slope2 [m/s]",
# "Standard Error of Slope1 [m/s]", "Standard Error of Slope 2 [m/s]"
np.savetxt(writefilename, data, delimiter = "\t")

