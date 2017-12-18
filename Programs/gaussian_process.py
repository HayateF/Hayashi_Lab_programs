import math
import numpy as np

#mu = 0	# mean value
#sigma = 3	# standard deviation

#np.random.seed(1)
#s = np.random.normal(mu, sigma)
#ss = np.random.RamdomState
#t = np.random.normal(mu, sigma)
#ts = np.random.RandomState
#u = np.random.normal(mu, sigma)
#us = np.random.RandomState
#print (s, t, u)
#print (ss, ts, us)

#a = np.random.normal(0, 10, 100)
#print (a)

#b = np.random.normal(0, 10, (3, 10))
#print (b)

sigma = 100
sample = int(1e+08)	##### max sample is 1e+07.
#np.random.seed(213)
#gauss = np.random.normal(0, sigma, 10000000)	# this is the limit of iteration
#gauss = np.power(gauss, 2)
#std = math.sqrt(np.mean(gauss))
#print (sigma, std)

#np.random.seed(300)
gauss1 = np.random.normal(0, sigma, sample)
print ("mean value of gauss 1 is", np.mean(gauss1))
#np.random.seed(200)
gauss2 = np.random.normal(0, sigma, sample)
print ("mean of gauss 2 is", np.mean(gauss2))
gauss3 = gauss1 * gauss2
correlation = np.mean(gauss3)
print (correlation)
print ("normalized correlation is", correlation / (sigma ** 2))
## normalized correlation should be delta function.
