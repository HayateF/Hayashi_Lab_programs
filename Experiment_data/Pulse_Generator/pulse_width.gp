set xrange [0:11]
set yrange [0:11]
set xtics 1
set ytics 1
set xlabel "Set pulse width [ns]"
set ylabel "Real pulse width [ns]"
unset key
set grid

f(x) = a * x + b
## perform fitting
fit [0:11] f(x) "pulse_width_+-16V_summary.dat" u 1:2 via a,b

plot "pulse_width_+-16V_summary.dat" u 1:2 title "" lc rgb "red" pt 7 ps 1.5
rep f(x) title "" lc rgb "black" lt 1 lw 1.5
 
