set xrange [0:55]
set yrange [-1:25]
set xtics 5
set ytics 5
set xlabel "Pulse voltage [V]"
set ylabel "Reflected pulse voltage [V]"
unset key
set grid

f(x) = a * x**3 + b * x**2 + c * x
## perform fitting
fit [-5:55] f(x) "reflection.txt" u 1:4 via a,b,c

plot "reflection.txt" u 1:4 title "" lc rgb "red" pt 7 ps 1.5
rep f(x) title "" lc rgb "black" lt 1 lw 1.5
 
