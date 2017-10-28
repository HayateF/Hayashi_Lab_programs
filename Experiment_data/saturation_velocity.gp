#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-40:40]
set yrange [-100:100]
set xtics 10
set ytics 20
set xlabel "Pulse Amp [V]"
set ylabel "Velocity [m/s]"
set key left top
set grid

#saturation velocity for positive up-down area
vDpu=70.0

vDpd=70.0
vDnu=-70.0
vDnd=-70.0

#saturation pulse amplitude
aDpu=5.0
aDpd=5.0
aDnu=-5.0
aDnd=-5.0

#threshold pulse voltage
aCpu=4.0
aCpd=4.0
aCnu=-4.0
aCnd=-4.0

vpu(x)=vDpu/sqrt(1+(aDpu/(x-aCpu))**2)
vpd(x)=vDpd/sqrt(1+(aDpd/(x-aCpd))**2)
vnu(x)=vDnu/sqrt(1+(aDnu/(x-aCnu))**2)
vnd(x)=vDnd/sqrt(1+(aDnd/(x-aCnd))**2)

# perform fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-36:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-36:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDnd, aDnd, aCnd

# to get summary of fitting
fit [0:36] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:36] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-36:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-36:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDnd, aDnd, aCnd

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

