#plot "04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:20 title "ch1"
#plot "04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:21 title "ch2"
#plot "04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:22 title "ch3"
set datafile separator ","
set xrange [-10:370]
set xtics 30
set xlabel "Position [deg]"
set ylabel "R_xx [Ohm]"
unset key
set grid

#resitance without SMR for channel 1
R0_1=100

R0_2=595.8
R0_3=100

#SMR amplitude
RS_1=0.01
RS_2=0.588
RS_3=0.01

#angle(position) offset [deg]
phi_1=90
phi_2=90
phi_3=90

#linear offset for resistance if necessary
a_1=-0.00
a_2=0.00001
a_3=0.0000

R_1(x)=R0_1+RS_1*sin(x*pi/180+phi_1)**2+a_1*x
R_2(x)=R0_2+RS_2*sin(x*pi/180+phi_2)**2+a_2*x
R_3(x)=R0_3+RS_3*sin(x*pi/180+phi_3)**2+a_3*x

# perform fitting
#fit [-100:400] [74:*] R_1(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:20 via R0_1, RS_1, phi_1
#fit [-100:400] [74:*] R_2(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:21 via R0_2, RS_2, phi_2
#fit [-100:400] [150:*] R_3(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:22 via R0_3, RS_3, phi_3

# fitting including linear offset
#fit [-100:400] [200:*] R_1(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:20 via R0_1, RS_1, phi_1, a_1
fit [-100:400] [290:*] R_2(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:21 via R0_2, RS_2, phi_2, a_2
#fit [-100:400] [74:*] R_3(x) "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:22 via R0_3, RS_3, phi_3, a_3

#plot "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:20 title "ch1", R_1(x)
plot "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:21 title "ch2", R_2(x)
#plot "< tail -n +34 04_ch1_A364-6_RxxHyz__ch2_A364-4_RxxHyz__ch3_A364-9_RxxHyz_Hrot_300K.dat" u 6:22 title "ch3", R_3(x)

