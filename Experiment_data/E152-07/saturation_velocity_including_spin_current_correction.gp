#plot "velocity_v1_51a.dat" u 9:12 title "up-down"
#plot "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-55:55]
set yrange [-200:200]
set xtics 10
set xlabel "Pulse Amp [V]"
set ylabel "Velocity [m/s]"
set key left top
set grid

#v_D / D
A=158996.9841
#V_D / D
B=5410

#DMI constant
Dpu=5e-04
Dpd=5e-04
Dnu=5e-04
Dnd=5e-04

#conversion coefficient of spin current to DMI constant
cpu=1.0e-05
cpd=1.0e-05
cnu=1.0e-05
cnd=1.0e-05

#threshold pulse voltage
aCpu=8.0
aCpd=8.0
aCnu=-8.0
aCnd=-8.0

vpu(x)=A*(Dpu+x*cpu)/sqrt(1+(B*(Dpu+x*cpu)/(x-aCpu))**2)
vpd(x)=A*(Dpd+x*cpd)/sqrt(1+(B*(Dpd+x*cpd)/(x-aCpd))**2)
vnu(x)=A*(-Dnu+x*cnu)/sqrt(1+(B*(Dnu+x*cnu)/(x-aCnu))**2)
vnd(x)=A*(-Dnd+x*cnd)/sqrt(1+(B*(Dnd+x*cnd)/(x-aCnd))**2)

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

# perform fitting
fit [0:33] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, cpu
fit [0:33] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, cpd
fit [-33:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, cnu
fit [-33:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnd, aCnd, cnd

# to get summary of fitting
#fit [0:33] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, cpu
#fit [0:33] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, cpd
#fit [-33:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, cnu
#fit [-33:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnd, aCnd, cnd

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

