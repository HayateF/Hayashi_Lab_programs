set xrange [0:35]
set yrange [0:0.45]
set xtics 5
set ytics 0.05
set xlabel "Pulse Amp [V]"
set ylabel "DMI [erg/cm^2]"
set key left top
set grid

D(x) = a * x**2 + b * x + c
c = 0.166

# perform fitting
#fit [0:35] D(x) "< tail -n +10 DMI_Field_2M.txt" u 1:6:7 via a, b, c
fit [0:35] D(x) "< tail -n +10 DMI_Field_2M.txt" u 1:6:7 via a, b

plot "< tail -n +10 DMI_Field_2M.txt" u 1:6:7 w ye, D(x) title "fitting curve"

