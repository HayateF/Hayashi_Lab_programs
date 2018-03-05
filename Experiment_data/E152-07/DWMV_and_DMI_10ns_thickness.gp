set xrange [0:3]
set yrange [0.0:0.5]
set xtics 0.5
set ytics 0.1
set mxtics
set xlabel "Ta thickness [nm]"
set ylabel "DMI [mJ / m^2]"
set xlabel font "Times, 25"
set ylabel font "Times, 25"
## font size 10 is the default
set xlabel offset 0, -0.5
set ylabel offset -3, 0
set tics font "Times, 25"
#set key left top
#set key invert
unset key
set grid

fp(x) = ap * x + bp
fn(x) = an * x + bn

# perform fitting
#fit [0:3] fp(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:10:11 via ap, bp
#fit [0:3] fn(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:12:13 via an, bn

# to get summary of fitting
#fit [0:3] fp(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:10:11 via ap, bp
#fit [0:3] fn(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:12:13 via an, bn

plot "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:28:29 w ye title "" lc rgb "red" pt 7 ps 3 
#plot "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:13:15 w ye title "negative current" lc rgb "blue" pt 5 ps 1.5
#rep "< tail -n +6 DWMV_and_DMI_10ns.txt" u 3:10:12 w ye title "positive current" lc rgb "red" pt 7 ps 1.5
#rep fp(x) title "fit +"
#rep fn(x) title "fit -"


