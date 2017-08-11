import numpy as np

data = np.loadtxt("velocity_v1_51a.dat", delimiter = "\t", usecols = (8, 11, 14), skiprows = 1)
# \t means tab
# column 9 is Pulse_Amp, column 12 is Slope1, column 15 is Slope2,
# but you have to note that the number starts from 0.

# You have to sort an input file by pulse amplitude in ascending order.
data = np.sort(data, axis = 0)
print (data)

