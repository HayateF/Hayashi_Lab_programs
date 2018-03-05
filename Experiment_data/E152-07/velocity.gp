plot "velocity_v1_51a.dat" u 9:12 title "up-down", "velocity_v1_51a.dat" u 9:15 title "down-up"
set xrange [-55:55]
set yrange [-200:200]
set xtics 10
set xlabel "Pulse Amp [V]"
set ylabel "Velocity [m/s]"
set key left top
set grid
rep
set term postscript eps enhanced color

