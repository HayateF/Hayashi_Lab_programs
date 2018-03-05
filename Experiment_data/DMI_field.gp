##plot "velocity+current.txt" u 9:12 title "+current up-down"
##plot "velocity-current.txt" u 9:15 title "-current down-up"
set xrange [-1500:1500]
set yrange [-400:400]
set xtics 300
set mxtics
set xlabel "Field [Oe]"
set ylabel "Velocity [m/s]"
set key center bottom
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
#fit [-1500:1500] [1:*] vpu(x) "< tail -n +2 velocity+current.txt" u 5:12 via Apu, Bpu
fit [-1500:1500] [1:*] vpd(x) "< tail -n +2 velocity+current.txt" u 5:15 via Apd, Bpd
#fit [-1500:1500] [*:-1] vnu(x) "< tail -n +2 velocity-current.txt" u 5:12 via Anu, Bnu
fit [-1500:1500] [*:-1] vnd(x) "< tail -n +2 velocity-current.txt" u 5:15 via And, Bnd

# to get summary of fitting
#fit [-1500:1500] [1:*] vpu(x) "< tail -n +2 velocity+current.txt" u 5:12 via Apu, Bpu
fit [-1500:1500] [1:*] vpd(x) "< tail -n +2 velocity+current.txt" u 5:15 via Apd, Bpd
#fit [-1500:1500] [*:-1] vnu(x) "< tail -n +2 velocity-current.txt" u 5:12 via Anu, Bnu
fit [-1500:1500] [*:-1] vnd(x) "< tail -n +2 velocity-current.txt" u 5:15 via And, Bnd

#plot "velocity+current.txt" u 5:12 title ""
plot "velocity+current.txt" u 5:15 title ""
#rep "velocity-current.txt" u 5:12 title ""
rep "velocity-current.txt" u 5:15 title ""
#rep vpu(x) title "+ up-down"
rep vpd(x) title "+ down-up"
#rep vnu(x) title "- up-down"
rep vnd(x) title "- down-up"

