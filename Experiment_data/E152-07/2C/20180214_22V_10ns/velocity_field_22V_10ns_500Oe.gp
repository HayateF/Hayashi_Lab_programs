##plot "velocity+current.txt" u 9:12 title "+current up-down"
##plot "velocity-current.txt" u 9:15 title "-current down-up"
set xrange [-1200:1200]
set yrange [-220:220]
set xtics 200
set mxtics
set ytics 50
set xlabel "Field [Oe]"
set ylabel "Velocity [m/s]"
set key center top
set grid

# correction factor from pulse width. But in this linear fitting, this factor does not have any effects on the x-intercepts.
f = 1.1

## Hall coefficient
Hall_a = 9.7687 * 1000
Hall_b = 249.7

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
fit [-550:550] [1:*] vpu(x) "< tail -n +2 up-down_Hx/velocity_up-down_+current.txt" u ($3 * Hall_a + Hall_b):($12 * f) via Apu, Bpu
fit [-550:550] [1:*] vpd(x) "< tail -n +2 down-up_Hx/velocity_down-up_+current.txt" u ($3 * Hall_a + Hall_b):($15 * f) via Apd, Bpd
fit [-550:550] [*:-1] vnu(x) "< tail -n +2 up-down_Hx/velocity_up-down_-current.txt" u ($3 * Hall_a + Hall_b):($12 * f) via Anu, Bnu
fit [-550:550] [*:-1] vnd(x) "< tail -n +2 down-up_Hx/velocity_down-up_-current.txt" u ($3 * Hall_a + Hall_b):($15 * f) via And, Bnd

# to get summary of fitting
fit [-550:550] [1:*] vpu(x) "< tail -n +2 up-down_Hx/velocity_up-down_+current.txt" u ($3 * Hall_a + Hall_b):($12 * f) via Apu, Bpu
fit [-550:550] [1:*] vpd(x) "< tail -n +2 down-up_Hx/velocity_down-up_+current.txt" u ($3 * Hall_a + Hall_b):($15 * f) via Apd, Bpd
fit [-550:550] [*:-1] vnu(x) "< tail -n +2 up-down_Hx/velocity_up-down_-current.txt" u ($3 * Hall_a + Hall_b):($12 * f) via Anu, Bnu
fit [-550:550] [*:-1] vnd(x) "< tail -n +2 down-up_Hx/velocity_down-up_-current.txt" u ($3 * Hall_a + Hall_b):($15 * f) via And, Bnd

plot "up-down_Hx/velocity_up-down_+current.txt" u ($3 * Hall_a + Hall_b):($12 * f) title "+ up-down" lc rgb "red" pt 7 ps 1.5
rep "down-up_Hx/velocity_down-up_+current.txt" u ($3 * Hall_a + Hall_b):($15 * f) title "+ down-up" lc rgb "red" pt 6 ps 1.5
rep "up-down_Hx/velocity_up-down_-current.txt" u ($3 * Hall_a + Hall_b):($12 * f) title "- up-down" lc rgb "blue" pt 5 ps 1.5
rep "down-up_Hx/velocity_down-up_-current.txt" u ($3 * Hall_a + Hall_b):($15 * f) title "- down-up" lc rgb "blue" pt 4 ps 1.5
rep vpu(x) title "" lc rgb "red" lt 1 lw 1.5
rep vpd(x) title "" lc rgb "red" lt 1 lw 1.5
rep vnu(x) title "" lc rgb "blue" lt 1 lw 1.5
rep vnd(x) title "" lc rgb "blue" lt 1 lw 1.5

