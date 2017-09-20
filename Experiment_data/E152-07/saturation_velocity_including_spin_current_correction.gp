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
Dpu=2e-04
Dpd=2e-04
Dnu=2e-04
Dnd=2e-04

#conversion coefficient of spin current to DMI constant
#cpu=1.0e-05
#cpd=1.0e-05
#cnu=1.0e-06
#cnd=1.0e-06
cpu=0
cpd=0
cnu=0
cnd=0

#threshold pulse voltage
aCpu=4.0
aCpd=4.0
aCnu=-5.0
aCnd=-5.0

#correction factor
Fpu=1.0
Fpd=1.0
Fnu=1.0
Fnd=1.0

vpu(x)=A*(Dpu+x*cpu)/sqrt(1+(Fpu*B*(Dpu+x*cpu)/(x-aCpu))**2)
vpd(x)=A*(Dpd+x*cpd)/sqrt(1+(Fpd*B*(Dpd+x*cpd)/(x-aCpd))**2)
vnu(x)=A*(-Dnu+x*cnu)/sqrt(1+(Fnu*B*(Dnu+x*cnu)/(x-aCnu))**2)
vnd(x)=A*(-Dnd+x*cnd)/sqrt(1+(Fnd*B*(Dnd+x*cnd)/(x-aCnd))**2)

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

# perform fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, Fpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, Fpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, Fnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnd, aCnd, Fnd

# to get summary of fitting
fit [0:30] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, Fpu
fit [0:30] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, Fpd
fit [-30:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, Fnu
fit [-30:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dnd, aCnd, Fnd

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

