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

#saturation velocity for positive up-down area
# v_D / D
Apu = 296881.8595
# V_D / D
Bpu = 11100

# DMI constant
Dpu(x) = (x < 25)? (a1 * (x - 25) + b) : (a2 * (x - 25) + b)
a1 = 0.00936854 / 1000
a2 = -0.00464041 / 1000
b = 0.372236 / 1000
#vDpu=30.0

vDpd=30.0
vDnu=-30.0
vDnd=-30.0

#saturation pulse amplitude
aDpu=5.0
aDpd=5.0
aDnu=-5.0
aDnd=-5.0

#threshold pulse voltage
aCpu=8.0
aCpd=8.0
aCnu=-8.0
aCnd=-8.0

#vpu(x)=vDpu/sqrt(1+(aDpu/(x-aCpu))**2)
#vpd(x)=vDpd/sqrt(1+(aDpd/(x-aCpd))**2)
vpu(x) = (x > aCpu)? (Apu * Dpu(x)) / sqrt(1+(Bpu * Dpu(x) / (x-aCpu))**2) : 0
#vpu(x) = (x > aCpu)? vDpu/sqrt(1+(aDpu/(x-aCpu))**2) : 0
vpd(x) = (x > aCpd)? vDpd/sqrt(1+(aDpd/(x-aCpd))**2) : 0
vnu(x) = (x < aCnu)? vDnu/sqrt(1+(aDnu/(x-aCnu))**2) : 0
vnd(x) = (x < aCnd)? vDnd/sqrt(1+(aDnd/(x-aCnd))**2) : 0

# perform fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aCpd
fit [-36:-10.5] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aCnu
fit [-36:-10.5] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aCnd

# to get summary of fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via Bpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aCpd
fit [-36:-10.5] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aCnu
fit [-36:-10.5] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aCnd

plot "velocity_v1_51a.dat" u 9:($15 * f) title "down-up" lc rgb "blue" pt 5 ps 3
rep "velocity_v1_51a.dat" u 9:($12 * f) title "up-down" lc rgb "red" pt 7 ps 3
rep vnd(x) title "fit - down-up" lc rgb "purple" lt 2 lw 1.5
rep vnu(x) title "fit - up-down" lc rgb "black" lt 4 lw 1.5
rep vpd(x) title "fit + down-up" lc rgb "purple" lt 2 lw 1.5
rep vpu(x) title "fit + up-down" lc rgb "black" lt 4 lw 1.5


