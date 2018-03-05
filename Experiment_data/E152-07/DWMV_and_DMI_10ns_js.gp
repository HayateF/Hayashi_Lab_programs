set term wxt
#set xrange [6e+10:9.5e+10]
set xrange [6:9.5]
set yrange [0.2:0.55]
#set xtics 0.5+10
set xtics 0.5
set ytics 0.05
set mxtics
set xlabel "Vertical Spin Current [10^{10} A/m^2]"
set ylabel "DMI [erg/cm^2]"
set key right bottom
set grid

f(x) = a * x + b
a = 0.1
b = 0.3

# perform fitting
#fit [7e+10:9.5e+10] f(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u 14:24:25 via a, b
fit [7:9.5] f(x) "< tail -n +6 DWMV_and_DMI_10ns.txt" u ($14/1e+10):24:25 via a, b

#a = a * 1e-10
plot "< tail -n +6 DWMV_and_DMI_10ns.txt" u ($14/1e+10):24:25 w ye title "average" lc rgb "red" pt 7 ps 1
rep f(x) title "fit" lc rgb "black" lw 1.5

set term png enhanced

