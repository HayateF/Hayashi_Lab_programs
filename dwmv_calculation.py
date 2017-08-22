from operator import itemgetter
import numpy as np

#################################################
########### main starts from here ###############
#################################################

data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", skiprows = 1)
#data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", usecols = (8, 9, 11, 14), skiprows = 1)
# \t means tab
# column 9 is Pulse_Amp, column 10 is Pulse length, column 12 is Slope1, column 15 is Slope2,
# but you have to note that the number starts from 0.
# So data[m][8] is m's Pulse Amplitude.

# You have to sort an input file by pulse amplitude in ascending order,
# and after that, by pulse length in ascending order..
# But if you sort with np.sort directly, you will sort all columns independently.
data = sorted(data, key = itemgetter(8, 9))
# itemgetter(8, 9) means sort by column 8 which is followed by sort by column 9.

# data = np.sort(data, axis = 0)	# axis = 0 means sort by column. axis = 1 means sort by row.
# np.sort does not suit this time because np.sort will sorts all columns independently.


n_longer = 1	# the number of rows that have longer pulse length
n_shorter = 1	# the number of rows that have shorter pulse length
current_length = 0	# When this is 0, we are at shorter pulse. When this is 1, we are at longer pulse.
current_row = 0	# the current row that we are reading
using_row = 0	# the row in which we will store data next

# We get (what is called in q-\Phi model) steady-state velocity as follows.
# Simply we calculate (t_l * v_l - t_s * v_s) / (t_l - t_s), where t is pulse width,
# v is velocity, subscript "l" means longer pulse, "s" means shorter pulse.
# Complexity below comes from multiple velocities of the same amplitude and pulse length.
# We calculate average when multiple velocities of the same amp and length exist.
t_l = 0.0
t_s = 0.0
v_lu = 0.0	# u means up-down
v_ld = 0.0	# d means down-up
v_su = 0.0
v_sd = 0.0

while current_row < len(data):
	if (data[current_row + 1][8] - data[current_row][8]) > 0.1:
		v_lu /= n_longer	# calculated average
		v_ld /= n_longer
		data[using_row][11] = (t_l * v_lu - t_s * v_su) / (t_l - t_s)	# get steady-state velocity
		data[using_row][12] = (t_l * v_ld - t_s * v_sd) / (t_l - t_s)
		using_row += 1
		n_longer = 1
		n_shorter = 1
		current_length = 0
		t_s = data[current_row + 1][9]
		v_lu = 0
		v_ld = 0
		v_su = 0
		v_sd = 0
	elif (data[current_row + 1][9] - data[current_row][9]) > 0.05:
		# This is true when we are reading shorter pulse, because the next pulse amp is higher and previous "if" works when we are readign longer pulse
		v_su /= n_shorter	# calculated average
		v_sd /= n_shorter
		current_length = 1
		t_l = data[current_row + 1][9]
	else:
		if current_length = 0:
			v_su += data[current_row][11]
			v_sd += data[current_row][12]
			# These sumation above lead to average later.
			n_shorter += 1
		elif current_length = 1:
			v_lu += data[current_row][11]
			v_ld += data[current_row][12]
			n_longer += 1

	current_row += 1





# Columns are the same as the original file.
# However, columns other than pulse amp, pulse length, slope1 and slope2
# do not have meaning because we calculated special values for velocities.
del data[using_row: len(data)]
# Delete list elements list[i] to list[j-1] by "del list[i: j]".
np.savetxt("real_velocity.dat", data, delimiter = "\t")

