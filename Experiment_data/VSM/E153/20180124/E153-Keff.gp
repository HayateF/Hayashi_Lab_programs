set xrange [-0.5:3.5]
set yrange [0:7]
set xtics 1
set xtics offset 0, -0.5
set ytics 1
set xlabel "Ta thickness (nm)"
set ylabel "{/Times-Italic K}_{eff} (10^5 J / m^3)"
set xlabel font "Times, 40"
set ylabel font "Times, 40"
## font size 10 is the default
set lmargin 13
set bmargin 6
set xlabel offset 0, -1.5
set ylabel offset -4, 0
set tics font "Times, 40"
set key left top
#set key invert
set grid

set label 1 at graph 0.03, 0.95 "(b)"
set label 1 font "Times, 40"

plot "Ms_and_Keff.txt" u 1:($4/100000) w linespoints title "" lc rgb "black" pt 5 ps 3

