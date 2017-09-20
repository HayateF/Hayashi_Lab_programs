#plot "velocity+current.txt" u 9:12 title "+current up-down"
#plot "velocity-current.txt" u 9:15 title "-current down-up"
set xrange [-750:750]
set yrange [*:*]
set xtics 200
set xlabel "Field [Oe]"
set ylabel "Velocity [m/s]"
set key center top
set grid

#slope for positive up-down area
Apu=0.0

Apd=0.0
Anu=0.0
And=0.0

#intercept
Bpu=0.0
Bpd=0.0
Bnu=0.0
Bnd=0.0


vpu(x)=Apu*x+Bpu
vpd(x)=Apd*x+Bpd
vnu(x)=Anu*x+Bnu
vnd(x)=And*x+Bnd

# perform fitting
fit [0:600] vpu(x) "< tail -n +2 velocity+current.txt" u 9:12 via Apu, Bpu
fit [0:600] vpd(x) "< tail -n +2 velocity+current.txt" u 9:15 via Apd, Bpd
fit [-600:0] vnu(x) "< tail -n +2 velocity-current.txt" u 9:12 via Anu, Bnu
fit [-600:0] vnd(x) "< tail -n +2 velocity-current.txt" u 9:15 via And, Bnd

# to get summary of fitting
fit [0:600] vpu(x) "< tail -n +2 velocity+current.txt" u 9:12 via Apu, Bpu
fit [0:600] vpd(x) "< tail -n +2 velocity+current.txt" u 9:15 via Apd, Bpd
fit [-600:0] vnu(x) "< tail -n +2 velocity-current.txt" u 9:12 via Anu, Bnu
fit [-600:0] vnd(x) "< tail -n +2 velocity-current.txt" u 9:15 via And, Bnd

plot "velocity+current.txt" u 9:12, "velocity+current.txt" u 9:15,\
"velocity-current.txt" u 9:12, "velocity-current.txt" u 9:15,\
vpu(x) title "fit + up-down", vpd(x) title "fit + down-up", vnu(x) title "fit - up-down", vnd(x) title "fit - down-up"

