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

#v_D / D
A=161773.1285
#V_D / D
B=5360

#DMI constant
Dpu=5e-04
Dpd=5e-04
Dnu=5e-04
Dnd=5e-04

#conversion coefficient of spin current to DMI constant
cpu=1.0e-06
cpd=1.0e-06
cnu=1.0e-06
cnd=1.0e-06

#threshold pulse voltage
aCpu=4.0
aCpd=4.0
aCnu=-4.0
aCnd=-4.0

#correction factor
Fpu=3
Fpd=3
Fnu=3
Fnd=3

vpu(x)=A*(Dpu+x*cpu)/sqrt(1+(Fpu*B*(Dpu+x*cpu)/(x-aCpu))**2)
vpd(x)=A*(Dpd+x*cpd)/sqrt(1+(Fpd*B*(Dpd+x*cpd)/(x-aCpd))**2)
vnu(x)=A*(-Dnu+x*cnu)/sqrt(1+(Fnu*B*(Dnu+x*cnu)/(x-aCnu))**2)
vnd(x)=A*(-Dnd+x*cnd)/sqrt(1+(Fnd*B*(Dnd+x*cnd)/(x-aCnd))**2)

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

# perform fitting
fit [0:26] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, Fpu, cpu
fit [0:26] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, Fpd, cpd
fit [-26:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, Fnu, cnu
fit [-26:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dnd, aCnd, Fnd, cnd

# to get summary of fitting
fit [0:26] vpu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dpu, aCpu, Fpu, cpu
fit [0:26] vpd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dpd, aCpd, Fpd, cpd
fit [-26:0] vnu(x) "< tail -n +2 velocity_v1_51a.dat" u 9:12 via Dnu, aCnu, Fnu, cnu
fit [-26:0] vnd(x) "< tail -n +2 velocity_v1_51a.dat" u 9:15 via Dnd, aCnd, Fnd, cnd

plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up", vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

