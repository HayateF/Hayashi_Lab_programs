##plot "velocity+current.txt" u 9:12 title "+current up-down"
##plot "velocity-current.txt" u 9:15 title "-current down-up"
set xrange [0:3]
set yrange [0:5]
set xtics 0.5
set mxtics
#set ytics 0.2
set ytics 1
set mytics
set xlabel "Ta thickness [nm]"
set ylabel "-R_{SMR} / s_F [%]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
#set lmargin 12
set lmargin 10
set bmargin 4
set xlabel offset 0, -0.5
set ylabel offset -3, 0
set tics font "Times, 25"
#set key center top
unset key
set grid

# resistivity [\mu \Omega cm]
rho_CFB = 160
rho_Ta = 200
rho_W = 120
# normalized conductivity
s_C = 1000 / rho_CFB
s_T = 1000 / rho_Ta
s_W = 1000 / rho_W

# thickness [nm]
t_C = 1
t_W = 1




plot "E152-05.dat" u 1:(-$2 * 100 / (t_C * s_C / (t_C * s_C + t_W * s_W + $1 * s_T))) title "" lc rgb "black" pt 7 ps 3
#rep "down-up/velocity+current.txt" u ($3 * Hall_a + Hall_b):($15 * f) title "+ down-up" lc rgb "red" pt 6 ps 3
#rep "up-down/velocity-current.txt" u ($3 * Hall_a + Hall_b):($12 * f) title "- up-down" lc rgb "blue" pt 5 ps 3
#rep "down-up/velocity-current.txt" u ($3 * Hall_a + Hall_b):($15 * f) title "- down-up" lc rgb "blue" pt 4 ps 3
#rep vpu(x) title "" lc rgb "red" lt 1 lw 1.5
#rep vpd(x) title "" lc rgb "red" lt 1 lw 1.5
#rep vnu(x) title "" lc rgb "blue" lt 1 lw 1.5
#rep vnd(x) title "" lc rgb "blue" lt 1 lw 1.5

