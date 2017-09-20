#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-55:55]
set yrange [-200:200]
set xtics 10
set xlabel "Pulse Amp [V]"
set ylabel "Velocity [m/s]"
set key left top
set grid

#saturation velocity for positive up-down area
vDpu=100.0

vDpd=100.0
vDnu=-50.0
vDnd=-50.0

#saturation pulse amplitude
aDpu=25.0
aDpd=25.0
aDnu=-25.0
aDnd=-25.0

#threshold pulse voltage
aCpu=8.0
aCpd=8.0
aCnu=-25.0
aCnd=-25.0

vpu(x)=vDpu/sqrt(1+(aDpu/(x-aCpu))**2)
vpd(x)=vDpd/sqrt(1+(aDpd/(x-aCpd))**2)
vnu(x)=vDnu/sqrt(1+(aDnu/(x-aCnu))**2)
vnd(x)=vDnd/sqrt(1+(aDnd/(x-aCnd))**2)

# perform fitting
fit [0:47] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:47] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-47:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-47:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnd, aDnd, aCnd

# to get summary of fitting
fit [0:47] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDpu, aDpu, aCpu
fit [0:47] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDpd, aDpd, aCpd
fit [-47:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via vDnu, aDnu, aCnu
fit [-47:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via vDnd, aDnd, aCnd

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

