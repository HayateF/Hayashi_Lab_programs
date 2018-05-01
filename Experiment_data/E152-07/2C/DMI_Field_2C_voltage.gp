## x is voltage
x_left = 0.0
x_right = 35.0
x_step = 5.0
set xrange [x_left:x_right]
set xtics x_step
#set mxtics
set xlabel "Pulse amplitude [V]"
set xlabel font "Times, 25"
set xlabel offset 0, -0.5

## y is DMI
y_up = 0.5
y_down = 0
set yrange [y_down:y_up]
set ytics 0.1
#set mytics
set ylabel "D [mJ / m^2]"
set ylabel font "Times, 25"
set ylabel offset -3, 0

#set rmargin 13
#set lmargin 13
set bmargin 4.2
set tmargin 4.2
set tics font "Times, 25"
set key left top
set grid



plot "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 w ye title "" lc rgb "black" pt 7 ps 3
#plot "< tail -n +10 DMI_Field_2C.txt" u 1:15:16 w ye title "" lc rgb "blue" pt 7 ps 3
#rep "< tail -n +10 DMI_Field_2C.txt" u 1:13:14 w ye title "" lc rgb "red" pt 7 ps 3

#D(x) = a * x**2 + b * x + c
boundary = 22
D(x) = (x < boundary)? (a1 * (x - boundary) + b) : (a2 * (x - boundary) + b)
fit [0:40] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a1, a2, b
rep D(x) title "" lc rgb "black" lt 1 lw 1.5

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
x2conv = 2 * ratio / ((resist + 50) * w * t_CFB * 1e-09) * 1e-12
set x2range [x_left * x2conv:x_right * x2conv] 
#set x2range [2 * x_left * ratio / ((resist + 50) * w * t_CFB * 1e-09) * 1e-12:2 * x_right * ratio / ((resist + 50) * w * t_CFB * 1e-09) * 1e-12]
set x2tics 0.3
set x2label "J_{FM} [10^{12} A/m^2]"
set x2label font "Times, 25"
set x2label offset 0, 0.7
set xtics nomirror

## y2 is the DMI field
# C = 10 if Oe, C = 1 if mT.
C = 1
set y2range [C * y_down / (Ms * sqrt(A / Keff)):C * y_up / (Ms * sqrt(A / Keff))]
set y2tics 20*C
#set y2label "H_{DM} [10^{-1} mT]"
set y2label "H_{DM} [mT]"
set y2label font "Times, 25"
set y2label offset 3, 0
set ytics nomirror

rep

rep "../../../Programs/DMI-J_C2-1.8e-06_9.1ns_2C.txt" u ($1 / x2conv):2 title "" lc rgb "black" pt 4 ps 3

#rep "< tail -n +10 DMI_Field_2C.txt" u 1:($12 * Ms * sqrt(A / Keff) / 10) title "STT correction" lc rgb "blue" pt 7 ps 1.5


#D(x) = a * x + b

# perform fitting
###fit [0:35] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b, c
###fit [0:35] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b, c
###fit [10:26] D(x) "< tail -n +10 DMI_Field_2C.txt" u 1:6:7 via a, b
#fit [5 * x2conv:23 * x2conv] D(x) "< tail -n +10 DMI_Field_2C.txt" u ($1 * x2conv):6:7 via a, b

#a = a * x2conv
#rep D(x) title "" lc rgb "black" lt 1 lw 1.5


