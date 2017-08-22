from operator import itemgetter
import numpy as np
readfilename = "velocity_v1_51a_20170821_3.dat"
writefilename = "real_velocity.dat"

#################################################
########### main starts from here ###############
#################################################

data = np.loadtxt(readfilename, delimiter = "\t", skiprows = 1)
#data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", usecols = (8, 9, 11, 14), skiprows = 1)
# \t means tab
# column 9 is Pulse_Amp, column 10 is Pulse length, column 12 is Slope1, column 15 is Slope2,
# but you have to note that the number starts from 0.
# So data[m][8] is m's Pulse Amplitude.

# You have to sort an input file by pulse amplitude in ascending order,
# and after that, by pulse length in ascending order..
# But if you sort with np.sort directly, you will sort all columns independently.
data = sorted(data, key = itemgetter(8, 9))
print ("sorted data is\n", data)
print ("data[0][8] is", data[0][8])
print ("data[0][9] is", data[0][9])
print ("data[1][8] is", data[1][8])
print ("data[1][9] is", data[1][9])

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
t_s = data[0][9]
v_lu = 0.0	# u means up-down
v_ld = 0.0	# d means down-up
v_su = 0.0
v_sd = 0.0

while current_row < len(data):
	if current_row == (len(data) - 1):
		v_lu = (v_lu + data[current_row][11]) / n_longer	# calculated average
		v_ld = (v_ld + data[current_row][14]) / n_longer
		data[using_row][11] = (t_l * v_lu - t_s * v_su) / (t_l - t_s)	# get steady-state velocity
		data[using_row][14] = (t_l * v_ld - t_s * v_sd) / (t_l - t_s)
		data[using_row][8] = data[current_row][8]
		data[using_row][9] = t_l - t_s
		using_row += 1
	elif (data[current_row + 1][8] - data[current_row][8]) > 0.1:
		v_lu = (v_lu + data[current_row][11]) / n_longer	# calculated average
		v_ld = (v_ld + data[current_row][14]) / n_longer
		data[using_row][11] = (t_l * v_lu - t_s * v_su) / (t_l - t_s)	# get steady-state velocity
		data[using_row][14] = (t_l * v_ld - t_s * v_sd) / (t_l - t_s)
		data[using_row][8] = data[current_row][8]
		data[using_row][9] = t_l - t_s

		using_row += 1
		n_longer = 1
		n_shorter = 1
		current_length = 0
		t_s = data[current_row + 1][9]
		v_lu = 0.0
		v_ld = 0.0
		v_su = 0.0
		v_sd = 0.0

	# When the pulse length of the next row is higher than that of the current row, there are 2 case.
	# This is because, for example, we have data such as 25V-3ns, 25V-3.5ns, 25V-4.5ns, 25V-5ns.
	# We have to distinguish the case of "3ns to 3.5ns", "3.5ns to 4.5ns", and "4.5ns to 5ns."
	elif (((data[current_row + 1][9] - data[current_row][9]) > 0.05) and (current_length == 1)):
		v_lu = (v_lu + data[current_row][11]) / n_longer	# calculated average
		v_ld = (v_ld + data[current_row][14]) / n_longer
		data[using_row][11] = (t_l * v_lu - t_s * v_su) / (t_l - t_s)	# get steady-state velocity
		data[using_row][14] = (t_l * v_ld - t_s * v_sd) / (t_l - t_s)
		data[using_row][8] = data[current_row][8]
		data[using_row][9] = t_l - t_s

		using_row += 1
		n_longer = 1
		n_shorter = 1
		current_length = 0
		t_s = data[current_row + 1][9]
		v_lu = 0.0
		v_ld = 0.0
		v_su = 0.0
		v_sd = 0.0
	elif (((data[current_row + 1][9] - data[current_row][9]) > 0.05) and (current_length == 0)):
		# This is true when we are reading shorter pulse, because the next pulse amp is higher and previous "if" works when we are readign longer pulse
		v_su = (v_su + data[current_row][11]) / n_shorter	# calculated average
		v_sd = (v_sd + data[current_row][14]) / n_shorter
		current_length = 1
		t_l = data[current_row + 1][9]
	else:
		if current_length == 0:
			v_su += data[current_row][11]
			v_sd += data[current_row][14]
			# These sumation above lead to average later.
			n_shorter += 1
		elif current_length == 1:
			v_lu += data[current_row][11]
			v_ld += data[current_row][14]
			n_longer += 1

	current_row += 1





# Columns are the same as the original file.
# However, columns other than pulse amp, pulse length, slope1 and slope2
# do not have meaning because we calculated special values for velocities.
del data[using_row: len(data)]
#print ("calculated results are\n", data)
# Delete list elements list[i] to list[j-1] by "del list[i: j]".
np.savetxt(writefilename, data, delimiter = "\t")

# Return to the original format.
orig_f = open(readfilename, "r")
str = orig_f.readline()
orig_f.close()
new_f = open(writefilename, "r")
content = new_f.read()
new_f.close()
new_f = open(writefilename, "w")
new_f.write(str)
new_f.write(content)
new_f.close()

