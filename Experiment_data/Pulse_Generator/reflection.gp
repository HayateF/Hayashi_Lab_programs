set xrange [0:55]
set yrange [-1:25]
set xtics 10
set mxtics
set ytics 5
set mytics
set xlabel "Pulse voltage [V]"
set ylabel "Reflected voltage [V]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
set lmargin 12
set bmargin 4
set xlabel offset 0, -0.5
set ylabel offset -3, -1
set tics font "Times, 25"
unset key
set grid

f(x) = a * x**3 + b * x**2 + c * x
## perform fitting
fit [-5:55] f(x) "reflection.txt" u 1:4 via a,b,c

plot "reflection.txt" u 1:4 title "" lc rgb "black" pt 7 ps 3
rep f(x) title "" lc rgb "black" lt 1 lw 1.5
 
