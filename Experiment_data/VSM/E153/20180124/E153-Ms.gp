set xrange [-0.5:3.5]
set yrange [0:1200]
set xtics 1
set xtics offset 0, -0.5
set ytics 300
set xlabel "Ta thickness (nm)"
#set ylabel "{/Times-Italic M}_s (10^3 J / Tm^3)"
set ylabel "{/Times-Italic M}_s (kA / m)"
set xlabel font "Times, 40"
set ylabel font "Times, 40"
## font size 10 is the default
set lmargin 14.5
set bmargin 6
set xlabel offset 0, -1.5
set ylabel offset -4, 0
set tics font "Times, 40"
set key left top
#set key invert
set grid

set label 1 at graph 0.03, 0.95 "(a)"
set label 1 font "Times, 40"

#plot "Ms_and_Keff.txt" u 1:($2/1000) w linespoints title "" lc rgb "black" pt 5 ps 3

plot "Ms_and_Keff.txt" u 1:($2/1000):($3/1000) w ye title "" lc rgb "black" pt 5 ps 3
rep "Ms_and_Keff.txt" u 1:($2/1000) w lines title "" lc rgb "black" lt 1 lw 1.5


