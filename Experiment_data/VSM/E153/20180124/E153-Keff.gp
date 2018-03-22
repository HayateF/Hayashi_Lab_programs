set xrange [-0.5:3.5]
set yrange [0:7]
set xtics 1
set ytics 1
set xlabel "Ta thickness [nm]"
set ylabel "K_{eff} [10^5 J / m^3]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
set xlabel offset 0, -0.5
set ylabel offset -3, 0
set tics font "Times, 25"
set key left top
#set key invert
set grid

plot "Ms_and_Keff.txt" u 1:($4/100000) w linespoints title "" lc rgb "black" pt 5 ps 3
