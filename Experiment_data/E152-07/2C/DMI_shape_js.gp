#set xrange [0:1.2e+11]
set xrange [0:12]
set yrange [0:0.45]
set xtics 0.2e+11
set ytics 0.05
set xlabel "Spin Current [A/m^2]"
set ylabel "DMI [erg/cm^2]"
set key left top
set grid

D(x) = a * x**2 + b * x + c
#a = -1e-23
#b = 3e-12
c = 0.2
a = -1e-03
b = 3e-02

# perform fitting
fit [0:1.2e+11] D(x) "< tail -n +10 DMI_Field_2C.txt" u ($8/1e+10):6:7 via a, b, c
#fit [0:35] D(x) "< tail -n +10 DMI_Field_2C.txt" u 8:6:7 via a, b, c

plot "< tail -n +10 DMI_Field_2C.txt" u ($8/1e+10):6:7 w ye, D(x) title "fitting curve"

