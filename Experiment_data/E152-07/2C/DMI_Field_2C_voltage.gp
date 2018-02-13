## x is voltage
x_left = 0.0
x_right = 35.0
x_step = 5.0
set xrange [x_left:x_right]
set xtics x_step
set xlabel "Pulse Amplitude [V]"

## y is DMI
y_up = 0.45
y_down = 0.2
set yrange [y_down:y_up]
set ytics 0.05
set ylabel "DMI [mJ / m^2]"

set key left top
set grid


#D(x) = a * x**2 + b * x + c
D(x) = a * x + b

# perform fitting
#fit [0:35] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b, c
#fit [0:35] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b, c
fit [10:26] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b

plot "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 w ye title "no correction" lc rgb "red" pt 7 ps 1
#rep D(x) title "" lc rgb "black" lt 1 lw 1.5


## the width of the nanowire [m]
w = 5e-06

## the length of the nanowire [m]
#L = 50e-06

## resistivity of Ta. unit is [\mu \Omega / cm]
rho_Ta = 200.0
## thickness of Ta [nm]
t_Ta = 2.3
## conductivity of Ta. unit is [S/m]
#sigma_Ta = 1e+08 / rho_Ta

## tungsten W
rho_W = 120.0
t_W = 1.0	
#sigma_W = 1e+08 / rho_W

## CoFeB ferromagnetic layer
rho_CFB = 160.0
t_CFB = 1.0
#sigma_CFB = 1e+08 / rho_CFB

## Measured resistance from domain wall motion [\Omega]
resist = 2778

## shunting ratio
ratio = t_CFB / (rho_CFB * (t_CFB / rho_CFB + t_W / rho_W + t_Ta / rho_Ta)) 

## Ms [J/Tm^3]
Ms = 1091757
## exchange stiffness [J/m]
A = 1.5e-11
## Keff [J/m^3]
Keff = 618799.413


## x2 is the current density in the ferromagnetic layer
#set x2range [x_left * sigma_CFB / L * 1e-12:x_right * sigma_CFB / L * 1e-12]
set x2range [2 * x_left * ratio / ((resist + 50) * w * t_CFB * 1e-09) * 1e-12:2 * x_right * ratio / ((resist + 50) * w * t_CFB * 1e-09) * 1e-12]
set x2tics 0.2
set x2label "Current Density in FM layer [10^{12} A/m^2]"
set xtics nomirror

## y2 is the DMI field
set y2range [10 * y_down / (Ms * sqrt(A / Keff)):10 * y_up / (Ms * sqrt(A / Keff))]
set y2tics 50
set y2label "DMI Field [Oe]"
set ytics nomirror

rep "< tail -n +10 DMI_Field_2C.txt" u 1:($12 * Ms * sqrt(A / Keff) / 10) title "STT correction" lc rgb "blue" pt 7 ps 1

rep

