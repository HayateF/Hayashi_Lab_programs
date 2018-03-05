set xrange [6:10]
set yrange [-0.05:0.5]
set xtics 0.5
set ytics 0.1
set xlabel "Time [ns]"
set ylabel "Voltage [a.u.]"
#set key left top
unset key
set grid
set datafile separator ","

#f(x) = a * x + b

# perform fitting
#fit [0:200] f(x) "pulse_width_+-16V_summary.dat" u 1:2 via a, b

plot "10.csv" u ($1 * 1e+09):2 title "" lc rgb "red" pt 7 ps 1
rep 0.45737 title "maximum" lc rgb "blue" lt 1 lw 1.5
rep 0.228685 title "half" lc rgb "blue" lt 1 lw 1.5
set arrow 1 from 6.713, -0.05 to 6.713, 0.5 nohead lc rgb "blue" lw 1.5
set arrow 2 from 8.138, -0.05 to 8.138, 0.5 nohead lc rgb "blue" lw 1.5
rep
#rep f(x) title "linear fit" lc rgb "black" lt 1 lw 1.5

