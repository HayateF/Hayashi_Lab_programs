#plot "SMR_ratio.txt" u 2:10:11 w ye
#set datafile separator ","
set xrange [0:9]
#set xtics 30
set xlabel "Ir Thickness [nm]"
set ylabel "R_S / R_xx [%]"
unset key
set grid

## spin diffusion length [nm]
lambda=5
## When lambda is dependent on rho_HM
#mu=30
#lambda(x)=mu/rho_HM(x)

# spin Hall angle
theta=0.038

# thickness of FM layer [nm]
t_FM=1

## resistivity of HM [\mu \Omega cm]
## in this case Ir
rho_HM=19
## When rho_HM is dependent on t_HM
#rho_HM(x)=(1e+08)/(1986810.22+439460.7*x)

## resistivity of FM [\mu \Omega cm]
## in this case CoFeB
rho_FM=150

#plot "SMR_ratio.txt" u 2:10:11, Percentage(x)

## for normal case
Percentage(x)=100*(theta**2)*(lambda/x)*(tanh(0.5*x/lambda)/(1+rho_HM*t_FM/(rho_FM*x)))*(1-1/cosh(x/lambda))
## perform fitting for nomal case
fit [0.5:8.5] [*:*] Percentage(x) "SMR_ratio.txt" u 2:10:11 via lambda, theta

## for the case where rho_HM is dependenet on t_HM
#Percentage(x)=100*(theta**2)*(lambda/x)*(tanh(0.5*x/lambda)/(1+rho_HM(x)*t_FM/(rho_FM*x)))*(1-1/cosh(x/lambda))
#fit [0.5:8.5] [*:*] Percentage(x) "SMR_ratio.txt" u 2:10:11 via lambda, theta

## for the case where rho_HM and lambda are dependent on t_HM
#Percentage(x)=100*(theta**2)*(lambda(x)/x)*(tanh(0.5*x/lambda(x))/(1+rho_HM(x)*t_FM/(rho_FM*x)))*(1-1/cosh(x/lambda(x)))
#fit [0.5:8.5] [*:*] Percentage(x) "SMR_ratio.txt" u 2:10:11 via mu, theta


plot "SMR_ratio.txt" u 2:10:11, Percentage(x)

