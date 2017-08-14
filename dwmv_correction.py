from operator import itemgetter
import numpy as np
SAMPLE_REF_RATE = 1.0
SMALL_CORRECTION = True	# when you correct velocities of small amplitudes, True, when not, False. 

# function returns the pulse voltage when you input a pulse with voltage v
def generator_ref(v):
	if v >= 0:
		return v ** 2 / 100.0
	else:
		return -1.0 * v ** 2 / 100.0


data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", usecols = (8, 11, 14), skiprows = 1)
# \t means tab
# column 9 is Pulse_Amp, column 12 is Slope1, column 15 is Slope2,
# but you have to note that the number starts from 0.

# You have to sort an input file by pulse amplitude in ascending order.
# But if you sort with np.sort directly, you will sort all columns independently.
data = sorted(data, key = itemgetter(0))	# you can replace "itemgetter(0)" to "lambda x: x[0]"
print ("sorted data is", data)

# data = np.sort(data, axis = 0)	# axis = 0 means sort by column. axis = 1 means sort by row.
# np.sort does not suit this time because np.sort will sorts all columns independently.

# Find the minimum positive pulse amplitude
MIN_POS_AMP_LIST = 0
for n in range(len(data)):
	if data[n][0] < 0.0:
		if data[n+1][0] > 0.0:
			MIN_POS_AMP_LIST = n+1
			break
print ("the list number of the minimum positive pulse amplitude is", MIN_POS_AMP_LIST)


# velocity correction for postivie pulse amplitude
# Note that you have to measure domain wall motion velocity at a certain pulse amplitude where the pulse reflection has little influence on the velocity.
# We do not calculate correction for the minimum positive pulse amplitude because we use the amplitude as the base.

m = MIN_POS_AMP_LIST + 1	# m is the list number that you want to correct.

# Correction is performed in the following way. We eliminate the velocity obtained by the reflection pulse.
# The velocity that we eliminate is determined by linear fitting
# between the closest amplitudes to the reflection amplitude.
# When the reflection amplitude is smaller than the minimum positive/negative amplitude,
# we consider that the reflection pulse does not have an influence on the velocity.

### WE HAVE TO CONSIDER THE SMALLER REFLECTION PULSE ###
# because smaller pulses can have an influence on velocities when domain walls are move.

while m < len(data):
	k = MIN_POS_AMP_LIST
	# k is the list number that you refer to when you correct m. Therefore, k is always satisfies k < m.
	ref_vol = SAMPLE_REF_RATE * generator_ref(data[m][0])
	
	# We consider the reflection pulse whose amplitude is larger than the minimum positive pulse amplitude.
	if ref_vol > data[MIN_POS_AMP_LIST][0]:		
		while k < len(data):
			if data[k][0] < ref_vol:
				if data[k+1][0] > ref_vol:			
					data[m][1] = data[m][1] - data[k][1] - (data[k+1][1] - data[k][1]) * (ref_vol - data[k][0]) / (data[k+1][0] - data[k][0])
					data[m][2] = data[m][2] - data[k][2] - (data[k+1][2] - data[k][2]) * (ref_vol - data[k][0]) / (data[k+1][0] - data[k][0])
					break
			k += 1
	elif SMALL_CORRECTION:
		print ("reflection voltage of", data[m][0], "is", ref_vol)
		print (data[m][1], "-", data[MIN_POS_AMP_LIST][1], "*", ref_vol, "/", data[MIN_POS_AMP_LIST][0], "is")
		data[m][1] = data[m][1] - data[MIN_POS_AMP_LIST][1] * ref_vol / data[MIN_POS_AMP_LIST][0]
		print (data[m][1])
		data[m][2] = data[m][2] - data[MIN_POS_AMP_LIST][2] * ref_vol / data[MIN_POS_AMP_LIST][0]
		
	m += 1


# velocity correction for negative pulse amplitude
# We have to correct from the smaller amplitude. In other words, we have to correct in order -8V, -12V, -20V, like that.

m = MIN_POS_AMP_LIST - 2

while m >= 0:
	k = MIN_POS_AMP_LIST - 1
	ref_vol = SAMPLE_REF_RATE * generator_ref(data[m][0])
	
	# We consider the reflection pulse whose amplitude is larger than the minimum negative pulse amplitude.
	if ref_vol < data[MIN_POS_AMP_LIST - 1][0]:		
		while k >= 0:
			if data[k][0] > ref_vol:
				if data[k-1][0] < ref_vol:			
					data[m][1] = data[m][1] - data[k][1] - (data[k-1][1] - data[k][1]) * (ref_vol - data[k][0]) / (data[k-1][0] - data[k][0])
					data[m][2] = data[m][2] - data[k][2] - (data[k-1][2] - data[k][2]) * (ref_vol - data[k][0]) / (data[k-1][0] - data[k][0])
					break
			k -= 1
	elif SMALL_CORRECTION:
		data[m][1] = data[m][1] - data[MIN_POS_AMP_LIST - 1][1] * ref_vol / data[MIN_POS_AMP_LIST - 1][0]
		data[m][2] = data[m][2] - data[MIN_POS_AMP_LIST - 1][2] * ref_vol / data[MIN_POS_AMP_LIST - 1][0]

	m -= 1

print (data)

#str = "Pulse_Amp[V]\tSlope_1\tSlope_2\n"
#with open("velocity_corrected.dat", "a") as f:
#	f.write(str)
#	np.savetxt(f, data, delimiter = "\t")
np.savetxt("velocity_corrected.dat", data, delimiter = "\t")

