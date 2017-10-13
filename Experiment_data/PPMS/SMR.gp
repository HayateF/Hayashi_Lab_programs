#plot "01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:20 title "ch1"
#plot "01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:21 title "ch2"
#plot "01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:22 title "ch3"
set xrange [-5:365]
set yrange [*:*]
set xtics 30
set xlabel "Position [deg]"
set ylabel "R_xx [Ohm]"
set key right top
set grid

#resitance without SMR for channel 1
R0_1=100

R0_2=100
R0_3=100

#SMR amplitude
RS_1=0.01
RS_2=0.01
RS_3=0.01

#angle(position) offset [deg]
phi_1=0
phi_2=0
phi_3=0

#linear offset for resistance if necessary
a_1=0
a_2=0
a_3=0

R_1(x)=R0_1+RS_1*cos(x*M_PI/90+phi_1)+a_1*x
R_2(x)=R0_2+RS_2*cos(x*M_PI/90+phi_2)+a_2*x
R_3(x)=R0_3+RS_3*cos(x*M_PI/90+phi_3)+a_3*x

# perform fitting
fit [-100:400] R_1(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:20 via R0_1, RS_1, phi_1
fit [-100:400] R_2(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:21 via R0_2, RS_2, phi_2
fit [-100:400] R_3(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:22 via R0_3, RS_3, phi_3

# to get summary of fitting
fit [-100:400] R_1(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:20 via R0_1, RS_1, phi_1
fit [-100:400] R_2(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:21 via R0_2, RS_2, phi_2
fit [-100:400] R_3(x) "< tail -n +34 01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:22 via R0_3, RS_3, phi_3


plot "01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:20 title "ch1",\
#"01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:21 title "ch2",\
#"01_ch1_A364-10_RxxHyz__ch2_A364-8_RxxHyz__ch3_A364-6_RxxHyz_Hrot_300K.dat" u 6:22 title "ch3",\
R_1(x),\
#R_2(x),\
#R_3(x)

