#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-35:35]
set yrange [-100:100]
set xtics 10
set ytics 25
set xlabel "Pulse amplitude [V]"
set ylabel "Velocity [m/s]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
set lmargin 13
set bmargin 4.5
set xlabel offset 0, -0.5
set ylabel offset -3, 0
set tics font "Times, 25"
#set key left top
#set key invert
unset key
set grid

#correction factor from pulse duration
f = 1.1

# v_D / D
A = 253348.612
# V_D / D
Bpu = 13900
Bpd = 13900
Bnu = 13900
Bnd = 13900
# DMI constant
#D(x) = apu * x**2 + bpu * x + cpu
Dp(x) = (x < 22)? (a1 * (x - 22) + b) : (a2 * (x - 22) + b)
Dn(x) = (x > -22)? (a1 * (x + 22) - b) : (a2 * (x + 22) - b)
a1 = 0.00452475 / 1000
a2 = -0.0102069 / 1000
b = 0.385581 / 1000


#threshold pulse voltage
aCpu = 8.0
aCpd = 8.0
aCnu = -4.0
aCnd = -4.0

vpu(x) = (x > aCpu)? (A * Dp(x)) / sqrt(1+(Bpu * Dp(x) / (x-aCpu))**2) : 0
vpd(x) = (x > aCpd)? (A * Dp(x)) / sqrt(1+(Bpd * Dp(x) / (x-aCpd))**2) : 0
vnu(x) = (x < aCnu)? (A * Dn(x)) / sqrt(1+(Bnu * Dn(x) / (x-aCnu))**2) : 0
vnd(x) = (x < aCnd)? (A * Dn(x)) / sqrt(1+(Bnd * Dn(x) / (x-aCnd))**2) : 0

#plot vpu(x)
#rep vnu(x)
#rep Dp(x)
#rep "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f)

# perform fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bpu, aCpu 
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via aCpd, Bpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via aCnu, Bnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via aCnd, Bnd




## saturation velocity for positive up-down are
vDpu = 30.0

vDpd = 30.0
vDnu = -30.0
vDnd = -30.0

## saturation pulse amplitude
aDpu = 5.0
aDpd = 5.0
aDnu = -5.0
aDnd = -5.0

## threshold pulse voltage
aTpu = 8.0
aTpd = 8.0
aTnu = -8.0
aTnd = -8.0

upu(x) = (x > aTpu)? vDpu / sqrt(1 + (aDpu / (x - aTpu))**2) : 0
upd(x) = (x > aTpd)? vDpd / sqrt(1 + (aDpd / (x - aTpd))**2) : 0
unu(x) = (x < aTnu)? vDnu / sqrt(1 + (aDnu / (x - aTnu))**2) : 0
und(x) = (x < aTnd)? vDnd / sqrt(1 + (aDnd / (x - aTnd))**2) : 0

## perfom fitting
fit [0:30] upu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aTpu 
fit [0:30] upd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aTpd
fit [-30:0] unu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aTnu
fit [-30:0] und(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aTnd




## to get summary of fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via aCpu, Bpu 
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via aCpd, Bpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via aCnu, Bnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via aCnd, Bnd

fit [0:30] upu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aTpu 
fit [0:30] upd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aTpd
fit [-30:0] unu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aTnu
fit [-30:0] und(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aTnd






plot "velocity_v1_51a.dat" u 9:($15 * f) title "down-up" lc rgb "blue" pt 5 ps 3
rep "velocity_v1_51a.dat" u 9:($12 * f) title "up-down" lc rgb "red" pt 7 ps 3
rep vnd(x) title "fit - down-up" lc rgb "purple" lt 2 lw 1
rep vnu(x) title "fit - up-down" lc rgb "black" lt 4 lw 1
rep vpd(x) title "fit + down-up" lc rgb "purple" lt 2 lw 1
rep vpu(x) title "fit + up-down" lc rgb "black" lt 4 lw 1
rep und(x) title "" lc rgb "purple" lt 1 lw 1.5
rep unu(x) title "" lc rgb "black" lt 1 lw 1.5
rep upd(x) title "" lc rgb "purple" lt 1 lw 1.5
rep upu(x) title "" lc rgb "black" lt 1 lw 1.5

