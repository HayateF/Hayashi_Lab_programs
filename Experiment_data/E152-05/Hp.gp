set xrange [0:3]
set yrange [0:20]
set xtics 1
set ytics 5
set mxtics
set mytics
set xlabel "Ta thickness [nm]"
set ylabel "H_p [Oe]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
set lmargin 11
set bmargin 4
set xlabel offset 0, -0.5
set ylabel offset -3, 0
set tics font "Times, 25"
set key left top
#set key invert
set grid

plot "Hp.dat" u 2:3 title "" lc rgb "black" pt 5 ps 3

#plot "Ms_and_Keff.txt" u 1:($2/1000) w linespoints title "" lc rgb "black" pt 5 ps 3

#plot "Ms_and_Keff.txt" u 1:($2/1000):($3/1000) w ye title "" lc rgb "black" pt 5 ps 3
#rep "Ms_and_Keff.txt" u 1:($2/1000) w lines title "" lc rgb "black" lt 1 lw 1.5


