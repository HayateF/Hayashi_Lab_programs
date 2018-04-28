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

# correction factor from pulse duration
f = 1.1

# v_D / D
A = 296881.8595
# V_D / D
Bpu = 11100
Bpd = 11100
Bnu = 11100
Bnd = 11100

# DMI constant
Dp(x) = (x < 25)? (a1 * (x - 25) + b) : (a2 * (x - 25) + b)
Dn(x) = (x > -25)? (a1 * (x + 25) - b) : (a2 * (x + 25) - b)
a1 = 0.00936854 / 1000
a2 = -0.00464041 / 1000
b = 0.372236 / 1000

#threshold pulse voltage
aCpu=8.0
aCpd=8.0
aCnu=-8.0
aCnd=-8.0

vpu(x) = (x > aCpu)? (A * Dp(x)) / sqrt(1+(Bpu * Dp(x) / (x-aCpu))**2) : 0
vpd(x) = (x > aCpd)? (A * Dp(x)) / sqrt(1+(Bpd * Dp(x) / (x-aCpd))**2) : 0
vnu(x) = (x < aCnu)? (A * Dn(x)) / sqrt(1+(Bnu * Dn(x) / (x-aCnu))**2) : 0
vnd(x) = (x < aCnd)? (A * Dn(x)) / sqrt(1+(Bnd * Dn(x) / (x-aCnd))**2) : 0

# perform fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via Bpd, aCpd
fit [-36:-10.5] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bnu, aCnu
fit [-36:-10.5] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via Bnd, aCnd



## saturation velocity for positive up-down area
vDpu = 30

vDpd = 30
vDnu = -30
vDnd= -30

## saturation pulse amplitude
aDpu = 5
aDpd = 5
aDnu = -5
aDnd = -5

## threshold pulse voltage
aTpu = 8
aTpd = 8
aTnu = -8
aTnd = -8

upu(x) = (x > aTpu)? vDpu / sqrt(1 + (aDpu / (x - aTpu))**2) : 0
upd(x) = (x > aTpd)? vDpd / sqrt(1 + (aDpd / (x - aTpd))**2) : 0
unu(x) = (x < aTnu)? vDnu / sqrt(1 + (aDnu / (x - aTnu))**2) : 0
und(x) = (x < aTnd)? vDnd / sqrt(1 + (aDnd / (x - aTnd))**2) : 0

## perform fitting
fit [0:36] upu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aTpu
fit [0:36] upd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aTpd
fit [-36:-10.5] unu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aTnu
fit [-36:-10.5] und(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aTnd




# to get summary of fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via Bpd, aCpd
fit [-36:-10.5] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bnu, aCnu
fit [-36:-10.5] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via Bnd, aCnd

fit [0:36] upu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aTpu
fit [0:36] upd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aTpd
fit [-36:-10.5] unu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aTnu
fit [-36:-10.5] und(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aTnd



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

