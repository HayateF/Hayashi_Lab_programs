#plot "conductance.txt" u 2:8:9 w ye
#set datafile separator ","
set xrange [0:9]
#set xtics 30
set yrange [0:*]
set xlabel "Ir Thickness [nm]"
set ylabel "Conductivity [S/m]"
unset key
set grid

# consult Althammer_Quantitative study...

# conductivity for an infinitely thick film [S/m]
sigma_inf=5000000

# mean-free path for an infinitely thick film [nm]
l_inf=4

# a parameter for a surface roughness amplitude [nm]
h=0.5

# a parameter describing the scattering at the interfaces
# p = 0  means the diffusive limit
p=0

# offset conductivity from the other layers
sigma_0=1

#plot "conductance.txt" u 2:8:9, sigma(x)

sigma(x) = sigma_0 + sigma_inf / (1 + 3 * (l_inf * (1 - p)) / (8 * (x - h)))

fit [1.5:8.5] [*:*] sigma(x) "conductance.txt" u 2:8:9 via sigma_inf, l_inf, h, sigma_0

plot "conductance.txt" u 2:8:9 w ye, sigma(x)

