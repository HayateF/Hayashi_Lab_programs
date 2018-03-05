#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-35:35]
set yrange [-90:90]
set xtics 5
set ytics 20
set xlabel "Pulse Amp [V]"
set ylabel "Velocity [m/s]"
set key left top
set key invert
set grid

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
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDnd, aDnd, aCnd

# to get summary of fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDnd, aDnd, aCnd

plot "velocity_v1_51a.dat" u 9:15 title "down-up" lc rgb "blue" pt 5 ps 1.5
rep "velocity_v1_51a.dat" u 9:12 title "up-down" lc rgb "red" pt 7 ps 1.5
rep vnd(x) title "fit - down-up" lc rgb "purple" lt 1 lw 1.5
rep vnu(x) title "fit - up-down" lc rgb "black" lt 1 lw 1.5
rep vpd(x) title "fit + down-up" lc rgb "purple" lt 1 lw 1.5
rep vpu(x) title "fit + up-down" lc rgb "black" lt 1 lw 1.5

