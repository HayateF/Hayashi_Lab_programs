## x is real pulse length
x_1 = 0
x_2 = 8
set xrange [x_1:x_2]
set xtics 1
set xlabel "Real pulse length [ns]"


#set yrange [80:130]
set yrange [80:180]
#set ytics 20
set ylabel "Velocity [m/s]"

set key right top
#set key invert
set grid

plot "velocity_v1_51a_20170825.txt" u 4:7:9 w ye title "average" lc rgb "black" pt 5 ps 1.5
rep "velocity_v1_51a_20170825.txt" u 4:5 title "original" lc rgb "red" pt 6 ps 1.5

## pulse length correction factors
a = 0.984158
b = -0.77541

## x2 is set pulse length
set x2range [(x_1 - b) / a:(x_2 - b) / a]
set x2tics 1
set x2label "Set pulse length [ns]"
set xtics nomirror

rep
