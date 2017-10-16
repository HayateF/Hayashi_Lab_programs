#plot "SMR_ratio.txt" u 2:10:11 w ye
#set datafile separator ","
set xrange [0:9]
#set xtics 30
set xlabel "Ir Thickness [nm]"
set ylabel "R_S / R_xx [%]"
unset key
set grid

# spin diffusion length [nm]
lambda=0.02

# spin Hall angle
theta=0.01

# thickness of FM layer [nm]
t_FM=1

# resistivity of HM [\mu \Omega cm]
# in this case Ir
rho_HM=19

# resistivity of FM [\mu \Omega cm]
# in this case CoFeB
rho_FM=150

Percentage(x)=100*(theta**2)*(lambda/x)*(tanh(0.5*x/lambda)/(1+rho_HM*t_FM/(rho_FM*x)))*(1-1/cosh(x/lambda))

# perform fitting
fit [1.5:*] [*:*] Percentage(x) "SMR_ratio.txt" u 2:10:11 via lambda, theta


plot "SMR_ratio.txt" u 2:10:11, Percentage(x)

