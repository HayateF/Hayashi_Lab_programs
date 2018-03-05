#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-35:35]
set yrange [-100:100]
set xtics 10
set ytics 25
set xlabel "Pulse Amplitude [V]"
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

#saturation velocity for positive up-down area
vDpu=30.0

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
vpu(x) = (x > aCpu)? vDpu/sqrt(1+(aDpu/(x-aCpu))**2) : 0
vpd(x) = (x > aCpd)? vDpd/sqrt(1+(aDpd/(x-aCpd))**2) : 0
vnu(x) = (x < aCnu)? vDnu/sqrt(1+(aDnu/(x-aCnu))**2) : 0
vnd(x) = (x < aCnd)? vDnd/sqrt(1+(aDnd/(x-aCnd))**2) : 0

# perform fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aCpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aCpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aCnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aCnd

# to get summary of fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDpu, aDpu, aCpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDpd, aDpd, aCpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($12 * f) via vDnu, aDnu, aCnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:($15 * f) via vDnd, aDnd, aCnd

plot "velocity_v1_51a.dat" u 9:($15 * f) title "down-up" lc rgb "blue" pt 5 ps 3
rep "velocity_v1_51a.dat" u 9:($12 * f) title "up-down" lc rgb "red" pt 7 ps 3
rep vnd(x) title "fit - down-up" lc rgb "purple" lt 2 lw 3
rep vnu(x) title "fit - up-down" lc rgb "black" lt 1 lw 3
rep vpd(x) title "fit + down-up" lc rgb "purple" lt 2 lw 3
rep vpu(x) title "fit + up-down" lc rgb "black" lt 1 lw 3

