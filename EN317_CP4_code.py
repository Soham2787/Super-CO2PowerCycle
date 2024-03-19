'''
Working Fluid: CO2
Cooling Fluid: Water

Assumed Parameters:
Wt, Et, Ec, Epc, p5, p6, p8, p10, p11, t5, t10, t11, t1, t3, effec_HTR

Variable Nomenclature:

Wt:                                     Turbine work output
Et:                                     Turbine isentropic efficiency
Rt:                                     Turbine pressure ratio

Wc:                                     Compressor work input
Ec:                                     Compressor isentropic efficiency
Rc:                                     Compressor pressure ratio

Wpc:                                    Pre-compressor work input
Epc:                                    Pre-compressor isentropic efficiency
Rpc:                                    Pre-compressor pressure ratio

pi:                                     stream pressure             i : [1, 11]
ti:                                     stream temperature          i : [1, 11]
hi:                                     stream specific enthalpy    i : [1, 11]
si:                                     stream specific entropy     i : [1, 11]

Cph_HTR:                                average Cp of HTR hot stream
Cpc_HTR:                                average Cp of HTR cold stream

Cph_LTR:                                average Cp of LTR hot stream
Cpc_LTR:                                average Cp of LTR cold stream

Cph_cooler:                             average Cp of cooler hot stream
Cpc_cooler:                             average Cp of cooler cold stream

effec_HTR:                              HTR assumed effectiveness
effec_HTR_calc_enthalpy:                HTR effectiveness calculated using enthalpies
effec_HTR_calc_Cp:                      HTR effectiveness calculated using Cp

effec_LTR_calc_enthalpy:                LTR effectiveness calculated using enthalpies
effec_LTR_calc_Cp:                      LTR effectiveness calculated using Cp

effec_cooler_calc_enthalpy:             cooler effectiveness calculated using enthalpies
effec_cooler_calc_Cp:                   cooler effectiveness calculated using Cp

Q_heater:                               Heater heat input

Q_HTR_hot:                              heat lost from HTR hot stream
Q_HTR_cold:                             heat gained in HTR cold stream
Q_HTR:                                  HTR heat duty

Q_LTR_hot:                              heat lost from LTR hot stream
Q_LTR_cold:                             heat gained in LTR cold stream
Q_LTR:                                  LTR heat duty

Q_cooler_hot:                           heat lost from cooler hot stream
Q_cooler_cold:                          heat gained in cooler cold stream
Q_cooler:                               cooler heat rejection

h_t3_p6:                                specific enthalpy of CO2 at t3 and p6
h_t2_p8:                                specific enthalpy of CO2 at t2 and p8
h_t10_p9:                               specific enthalpy of CO2 at t10 and p9

w_fluid:                                working fluid
Mco2:                                   working fluid flow rate

c_fluid:                                cooling fluid
Mwater:                                 cooling fluid flow rate

'''
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import numpy as np

#Assumed Parameters
Wt = 100*1000000      #Turbine work output

Et = 0.9            #Turbine efficiency
Ec = 0.85           #Compressor efficiency
Epc = 0.85          #Precomp efficiency

p5 = 250*100000     #Turbine inlet pressure
p6 = 90*100000      #Turbine outlet pressure
p8 = 120*100000     #Precomp outlet pressure
p10 = 1.36*100000   #Cooler inlet pressure
p11 = 1.36*100000   #Cooler outlet pressure

t5 = 560 + 273      #TIT
t10 = 20 + 273      #Cooler inlet temp
t11 = 30 +273       #Cooler outlet temp
t1 = 35 + 273       #Compressor inlet temp
t3 = 264 + 273      #Cold HTR inlet temp
effec_HTR = 0.8     #effectiveness of HTR
w_fluid = 'CO2'     #Working Fluid - CO2
c_fluid = 'Water'   #Cooling Fluid - Water


#PRESSURES
Rt = p6/p5
print("Turbine pressure Ratio = ", 1/Rt)

p7 = p6
Rpc = p8/p7
print("Precompressor pressure ratio = ", Rpc, '\n')

p9 = p8
p1 = p9

p4 = p5
p3 = p4
p2 = p3

Rc = p2/p1
print("Compressor pressure ratio = ", Rc, '\n')


#Known enthalpies and entropies

#Stream 5
h5 = CP.PropsSI('H', 'P', p5, 'T', t5, w_fluid)
s5 = CP.PropsSI('S', 'P', p5, 'T', t5, w_fluid)

print("STREAM 5:", '\n')
print("t5 = ", int(t5) - 273, '°C')
print("p5 = ", p5/100000, 'bar')
print("h5 = ", round(h5/1000 ,2), 'kJ/kg')
print("s5 = ", s5/1000, 'kJ/kg - K', '\n')

#Stream 3
h3 = CP.PropsSI('H', 'P', p3, 'T', t3, w_fluid)
s3 = CP.PropsSI('S', 'P', p3, 'T', t3, w_fluid)

print("STREAM 3:", '\n')
print("t3 = ", int(t3) - 273, '°C')
print("p3 = ", p3/100000, 'bar')
print("h3 = ", round(h3/1000, 2), 'kJ/kg')
print("s3 = ", s3/1000, 'kJ/kg - K', '\n')


#Stream 1
h1 = CP.PropsSI('H', 'P', p1, 'T', t1, w_fluid)
s1 = CP.PropsSI('S', 'P', p1, 'T', t1, w_fluid)

print("STREAM 1:", '\n')
print("t1 = ", int(t1) - 273, '°C')
print("p1 = ", p1/100000, 'bar')
print("h1 = ", round(h1/1000, 2), 'kJ/kg')
print("s1 = ", s1/1000, 'kJ/kg - K', '\n')

#Stream 10
h10 = CP.PropsSI('H', 'P', p10, 'T', t10, c_fluid)
s10 = CP.PropsSI('S', 'P', p10, 'T', t10, c_fluid)

print("STREAM 10:", '\n')
print("t10 = ", int(t10) - 273, '°C')
print("p10 = ", p10/100000, 'bar')
print("h10 = ", round(h10/1000, 2), 'kJ/kg')
print("s10 = ", s10/1000, 'kJ/kg - K', '\n')

#Stream 11
h11 = CP.PropsSI('H', 'P', p11, 'T', t11, c_fluid)
s11 = CP.PropsSI('S', 'P', p11, 'T', t11, c_fluid)

print("STREAM 11:", '\n')
print("t11 = ", int(t11) - 273, '°C')
print("p11 = ", p11/100000, 'bar')
print("h11 = ", round(h11/1000, 2), 'kJ/kg')
print("s11 = ", s11/1000, 'kJ/kg - K', '\n')

#TURBINE
h6s = CP.PropsSI('H', 'P', p6, 'S', s5, w_fluid)
h6 = h5 - (Et*(h5 - h6s))
t6 = CP.PropsSI('T', 'P', p6, 'H', h6, w_fluid)
s6 = CP.PropsSI('S', 'P', p6, 'T', t6, w_fluid)

#Stream 6
print("STREAM 6:", '\n')
print("t6 = ", int(t6) - 273, '°C')
print("p6 = ", p6/100000, 'bar')
print("h6 = ", round(h6/1000, 2), 'kJ/kg')
print("s6 = ", s6/1000, 'kJ/kg - K', '\n')

Mco2 = Wt/(h5 - h6)
print("CO2 flow rate = ", round(Mco2, 2), 'kg/s', '\n')

#HTR
h_t3_p6 = CP.PropsSI('H', 'P', p6, 'T', t3, w_fluid)

h7 = h6 - (effec_HTR*(h6 - h_t3_p6))

t7 = CP.PropsSI('T', 'P', p7, 'H', h7, w_fluid)
s7 = CP.PropsSI('S', 'P', p7, 'T', t7, w_fluid)

#Stream 7
print("STREAM 7:", '\n')
print("t7 = ", int(t7) - 273, '°C')
print("p7 = ", p7/100000, 'bar')
print("h7 = ", round(h7/1000, 2), 'kJ/kg')
print("s7 = ", s7/1000, 'kJ/kg - K', '\n')

h4 = h3 + (h6 - h7)

t4 = CP.PropsSI('T', 'P', p4, 'H', h4, w_fluid)
s4 = CP.PropsSI('S', 'P', p4, 'T', t4, w_fluid)

#Stream 4
print("STREAM 4:", '\n')
print("t4 = ", int(t4) - 273, '°C')
print("p4 = ", p4/100000, 'bar')
print("h4 = ", round(h4/1000, 2), 'kJ/kg')
print("s4 = ", s4/1000, 'kJ/kg - K', '\n')

#Precompressor
h8s = CP.PropsSI('H', 'P', p8, 'S', s7, w_fluid)
h8 = ((h8s - h7)/Epc) + h7

t8 = CP.PropsSI('T', 'P', p8, 'H', h8, w_fluid)
s8 = CP.PropsSI('S', 'P', p8, 'T', t8, w_fluid)

#Stream 8
print("STREAM 8:", '\n')
print("t8 = ", int(t8) - 273, '°C')
print("p8 = ", p8/100000, 'bar')
print("h8 = ", round(h8/1000, 2), 'kJ/kg')
print("s8 = ", s8/1000, 'kJ/kg - K', '\n')

#Compressor
h2s = CP.PropsSI('H', 'P', p2, 'S', s1, w_fluid)
h2 = ((h2s - h1)/Ec) + h1

t2 = CP.PropsSI('T', 'P', p2, 'H', h2, w_fluid)
s2 = CP.PropsSI('S', 'P', p2, 'T', t2, w_fluid)

#Stream 2
print("STREAM 2:", '\n')
print("t2 = ", int(t2) - 273, '°C')
print("p2 = ", p2/100000, 'bar')
print("h2 = ", round(h2/1000, 2), 'kJ/kg')
print("s2 = ", s2/1000, 'kJ/kg - K', '\n')

#LTR
h9 = h8 - (h3 - h2)

t9 = CP.PropsSI('T', 'P', p9, 'H', h9, w_fluid)
s9 = CP.PropsSI('S', 'P', p9, 'T', t9, w_fluid)

#Stream 9
print("STREAM 9:", '\n')
print("t9 = ", int(t9) - 273, '°C')
print("p9 = ", p9/100000, 'bar')
print("h9 = ", round(h9/1000, 2), 'kJ/kg')
print("s9 = ", s9/1000, 'kJ/kg - K', '\n')


#Cooler
Mwater = Mco2*(h9 - h1)/(h11 - h10)

print("Cooling water flow rate = ", round(Mwater, 2), 'kg/s', '\n')


#Work Results
print("Turbine work output =", Wt/1000000, "MW")

Wpc = Mco2*(h8 - h7)        #Precomp work input
print("Precompressor work input = ", round(Wpc/1000000, 3), 'MW')

Wc = Mco2*(h2 - h1)         #Compressor work input
print("Compressor work input = ", round(Wc/1000000, 3), 'MW')

Wnet = Wt - Wc - Wpc
print("Net cycle work output = ", round(Wnet/1000000, 3), 'MW', '\n')

E_cycle = (Wt - Wc - Wpc)/(Mco2*(h5 - h4))      #Cycle efficiency
print("Cycle efficiency = ", round(E_cycle*100, 3), '%', '\n')

#Heat Duties
Q_heater = Mco2*(h5 - h4)       #Heater heat input
print("Heater heat input = ", round(Q_heater/1000000, 3), 'MW')

Q_HTR_hot = Mco2*(h6 - h7)
Q_HTR_cold = Mco2*(h4 - h3)
Q_HTR = (Q_HTR_hot + Q_HTR_cold)/2
print("HTR heat duty = ", round(Q_HTR/1000000, 3), 'MW')

Q_LTR_hot = Mco2*(h8 - h9)
Q_LTR_cold = Mco2*(h3 - h2)
Q_LTR = (Q_LTR_hot + Q_LTR_cold)/2
print("LTR heat duty = ", round(Q_LTR/1000000, 3), 'MW')

Q_cooler_hot = Mco2*(h9 - h1)
Q_cooler_cold = Mwater*(h11 - h10)
Q_cooler = (Q_cooler_hot + Q_cooler_cold)/2
print("Cooler heat rejection = ", round(Q_cooler/1000000, 3), 'MW', '\n')

#Effectiveness Results
#HTR effectiveness:

effec_HTR_calc_enthalpy = (h6 - h7)/(h6 - h_t3_p6)       #Using enthalpies
print("effectiveness of HTR (using enthalpies) = ", round(effec_HTR_calc_enthalpy, 4))

#using Cp
Cph_HTR = (h6 - h7)/(t6 - t7)
Cpc_HTR = (h4 - h3)/(t4 - t3)

if (Cph_HTR < Cpc_HTR):
    effec_HTR_calc_Cp = (t6 - t7)/(t6 - t3)
if (Cph_HTR > Cpc_HTR):
    effec_HTR_calc_Cp = (t4 - t3)/(t6 - t3)

print("effectiveness of HTR (using Cp) = ", round(effec_HTR_calc_Cp, 4), '\n')

# LTR effectiveness:
h_t2_p8 = CP.PropsSI('H', 'P', p8, 'T', t2, w_fluid)
effec_LTR_calc_enthalpy = (h8 - h9) / (h8 - h_t2_p8)  # Using enthalpies
print("effectiveness of LTR (using enthalpies) = ", round(effec_LTR_calc_enthalpy, 4))

#using Cp
Cph_LTR = (h8 - h9) / (t8 - t9)
Cpc_LTR = (h3 - h2)/ (t3 - t2)

if (Cph_LTR < Cpc_LTR):
    effec_LTR_calc_Cp = (t8 - t9) / (t8 - t2)
if (Cph_LTR > Cpc_LTR):
    effec_LTR_calc_Cp = (t3 - t2) / (t8 - t2)

print("effectiveness of LTR (using Cp) = ", round(effec_LTR_calc_Cp, 4), '\n')

#Cooler effectiveness
h_t10_p9 = CP.PropsSI('H', 'P', p9, 'T', t10, w_fluid)
effec_cooler_calc_enthalpy = (h9 - h1)/(h9 - h_t10_p9)                  #using enthalpies
print("effectiveness of cooler (using enthalpies) = ", round(effec_cooler_calc_enthalpy, 4))

#using Cp
Cph_cooler = (h9 - h1)/(t9 - t1)
Cpc_cooler = (h11 - h10)/(t11 - t10)

if(Mco2*Cph_cooler < Mwater*Cpc_cooler):
    effec_cooler_calc_Cp = (t9 - t1)/(t9 - t10)
if(Mco2*Cph_cooler > Mwater*Cpc_cooler):
    effec_cooler_calc_Cp = (t11 - t10)/(t9 - t10)

print("effectiveness of cooler (using Cp) = ", round(effec_cooler_calc_Cp, 4), '\n')


#T-s plot


y=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t1]
x=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s1]
plt.scatter(x, y,)
plt.plot(x, y, linestyle = 'dashed',)
plt.ylabel('Temperature (K)')
plt.xlabel('Entropy (J/kg.K)')
i=1
for (xi, yi) in zip(x, y):
    if (i<10):
        plt.text(xi, yi, i, va='bottom', ha='center')
        i=i+1
plt.grid()
plt.show()

#HTR Temperature Profile
Hc = h3
Hh = h7
n = 25
Qn = Q_HTR/n
temperatures_cold_HTR =[int(t3) -273]
temperatures_hot_HTR = [int(t7)-273]
j_values = []

j = 0
while(j < n ):
    Hc += Qn/Mco2
    Tc = CP.PropsSI('T', 'H', Hc, 'P', p3, 'CO2')
    temperatures_cold_HTR.append(int(Tc)-273)

    Hh += Qn/Mco2
    Th = CP.PropsSI('T', 'H', Hh, 'P', p6, 'CO2')
    temperatures_hot_HTR.append(int(Th)-273)

    j_values.append(j)
    j += 1

j_values.append(j)


plt.figure(figsize = (8,6))

plt.plot(j_values, temperatures_cold_HTR, label='COLD', marker='o')
plt.plot(j_values, temperatures_hot_HTR, label='HOT', marker='s')
plt.xlabel('Division Number')

for i in range(len(j_values)):
    plt.text(j_values[i],temperatures_cold_HTR[i], str(temperatures_cold_HTR[i]), ha='right', va='bottom', fontsize=9)
    plt.text(j_values[i], temperatures_hot_HTR[i], str(temperatures_hot_HTR[i]), ha='right', va='top', fontsize=9)

plt.ylabel('Temperature (degrees Celcius)')
plt.twinx()
plt.ylabel('')

plt.grid(True, which = 'both')
plt.legend(loc = 'upper left')
plt.title('Temperature Profile HTR')


plt.show()

#LTR temperature profile
Hc_LTR= h2
Hh_LTR = h9
m = 25
Qn_LTR = Q_LTR/n
temperatures_cold_LTR =[int(t2) -273]
temperatures_hot_LTR = [int(t9)-273]
k_values = []

k = 0
while(k < m ):
    Hc_LTR += Qn_LTR/Mco2
    Tc_LTR = CP.PropsSI('T', 'H', Hc_LTR, 'P', p2, 'CO2')
    temperatures_cold_LTR.append(int(Tc_LTR)-273)

    Hh_LTR += Qn_LTR/Mco2
    Th_LTR = CP.PropsSI('T', 'H', Hh_LTR, 'P', p8, 'CO2')
    temperatures_hot_LTR.append(int(Th_LTR)-273)

    k_values.append(k)
    k += 1

k_values.append(k)


plt.figure(figsize = (8, 6))

plt.plot(k_values, temperatures_cold_LTR, label='COLD', marker='o')
plt.plot(k_values, temperatures_hot_LTR, label='HOT', marker='s')
plt.xlabel('Division Number')

for i in range(len(k_values)):
    plt.text(k_values[i],temperatures_cold_LTR[i], str(temperatures_cold_LTR[i]), ha='right', va='bottom', fontsize=9)
    plt.text(k_values[i], temperatures_hot_LTR[i], str(temperatures_hot_LTR[i]), ha='right', va='top', fontsize=9)

plt.ylabel('Temperature (degrees Celcius)')
plt.twinx()
plt.ylabel('')

plt.grid(True, which = 'both')
plt.legend(loc = 'upper left')
plt.title('Temperature Profile LTR')

# Display the plot
plt.show()

#Cooler temperature profile

Hc_cooler = h10
Hh_cooler = h1
o = 25
Qn_cooler = Q_cooler/o
temperatures_cold_cooler =[int(t10) -273]
temperatures_hot_cooler = [int(t1)-273]
l_values = []

l = 0
while(l < o ):
    Hc_cooler += Qn_cooler/Mco2
    Tc_cooler = CP.PropsSI('T', 'H', Hc_cooler, 'P', p10, 'Water')
    temperatures_cold_cooler.append(int(Tc_cooler)-273)

    Hh_cooler += Qn_cooler/Mco2
    Th_cooler = CP.PropsSI('T', 'H', Hh_cooler, 'P', p1, 'CO2')
    temperatures_hot_cooler.append(int(Th_cooler)-273)

    l_values.append(l)
    l += 1

l_values.append(l)


plt.figure(figsize = (8, 6))

plt.plot(l_values, temperatures_cold_cooler, label='COLD', marker='o')
plt.plot(l_values, temperatures_hot_cooler, label='HOT', marker='s')
plt.xlabel('Division Number')

for i in range(len(l_values)):
    plt.text(l_values[i],temperatures_cold_cooler[i], str(temperatures_cold_cooler[i]), ha='right', va='bottom', fontsize=9)
    plt.text(l_values[i], temperatures_hot_cooler[i], str(temperatures_hot_cooler[i]), ha='right', va='top', fontsize=9)

plt.ylabel('Temperature (degrees Celcius)')
plt.twinx()
plt.ylabel('')

plt.grid(True, which = 'both')
plt.legend(loc = 'upper left')
plt.title('Temperature Profile cooler')

# Display the plot
plt.show()



#Parametric Study
t5_values = np.linspace(460 + 273, 660 + 273, 10)

t5_values_plot = []
E_cycle_values = []

for t5 in t5_values:
    Wt = 100 * 1000000  # Turbine work output

    Et = 0.9  # Turbine efficiency
    Ec = 0.85  # Compressor efficiency
    Epc = 0.85  # Precomp efficiency

    p5 = 250 * 100000  # Turbine inlet pressure
    p6 = 90 * 100000  # Turbine outlet pressure
    p8 = 120 * 100000  # Precomp outlet pressure
    p10 = 1.36 * 100000  # Cooler inlet pressure
    p11 = 1.36 * 100000  # Cooler outlet pressure


    t10 = 20 + 273  # Cooler inlet temp
    t11 = 30 + 273  # Cooler outlet temp
    t1 = 35 + 273  # Compressor inlet temp
    t3 = 264 + 273  # Cold HTR inlet temp
    effec_HTR = 0.8  # effectiveness of HTR
    w_fluid = 'CO2'  # Working Fluid - CO2
    c_fluid = 'Water'  # Cooling Fluid - Water

    # PRESSURES
    Rt = p6 / p5


    p7 = p6
    Rpc = p8 / p7


    p9 = p8
    p1 = p9

    p4 = p5
    p3 = p4
    p2 = p3

    Rc = p2 / p1


    # Known enthalpies and entropies

    # Stream 5
    h5 = CP.PropsSI('H', 'P', p5, 'T', t5, w_fluid)
    s5 = CP.PropsSI('S', 'P', p5, 'T', t5, w_fluid)


    # Stream 3
    h3 = CP.PropsSI('H', 'P', p3, 'T', t3, w_fluid)
    s3 = CP.PropsSI('S', 'P', p3, 'T', t3, w_fluid)


    # Stream 1
    h1 = CP.PropsSI('H', 'P', p1, 'T', t1, w_fluid)
    s1 = CP.PropsSI('S', 'P', p1, 'T', t1, w_fluid)


    # Stream 10
    h10 = CP.PropsSI('H', 'P', p10, 'T', t10, c_fluid)
    s10 = CP.PropsSI('S', 'P', p10, 'T', t10, c_fluid)


    # Stream 11
    h11 = CP.PropsSI('H', 'P', p11, 'T', t11, c_fluid)
    s11 = CP.PropsSI('S', 'P', p11, 'T', t11, c_fluid)


    # TURBINE
    h6s = CP.PropsSI('H', 'P', p6, 'S', s5, w_fluid)
    h6 = h5 - (Et * (h5 - h6s))
    t6 = CP.PropsSI('T', 'P', p6, 'H', h6, w_fluid)
    s6 = CP.PropsSI('S', 'P', p6, 'T', t6, w_fluid)


    Mco2 = Wt / (h5 - h6)


    # HTR
    h_t3_p6 = CP.PropsSI('H', 'P', p6, 'T', t3, w_fluid)

    h7 = h6 - (effec_HTR * (h6 - h_t3_p6))

    t7 = CP.PropsSI('T', 'P', p7, 'H', h7, w_fluid)
    s7 = CP.PropsSI('S', 'P', p7, 'T', t7, w_fluid)


    h4 = h3 + (h6 - h7)

    t4 = CP.PropsSI('T', 'P', p4, 'H', h4, w_fluid)
    s4 = CP.PropsSI('S', 'P', p4, 'T', t4, w_fluid)


    # Precompressor
    h8s = CP.PropsSI('H', 'P', p8, 'S', s7, w_fluid)
    h8 = ((h8s - h7) / Epc) + h7

    t8 = CP.PropsSI('T', 'P', p8, 'H', h8, w_fluid)
    s8 = CP.PropsSI('S', 'P', p8, 'T', t8, w_fluid)

    # Compressor
    h2s = CP.PropsSI('H', 'P', p2, 'S', s1, w_fluid)
    h2 = ((h2s - h1) / Ec) + h1

    t2 = CP.PropsSI('T', 'P', p2, 'H', h2, w_fluid)
    s2 = CP.PropsSI('S', 'P', p2, 'T', t2, w_fluid)


    # LTR
    h9 = h8 - (h3 - h2)

    t9 = CP.PropsSI('T', 'P', p9, 'H', h9, w_fluid)
    s9 = CP.PropsSI('S', 'P', p9, 'T', t9, w_fluid)

    # Stream 9


    # Cooler
    Mwater = Mco2 * (h9 - h1) / (h11 - h10)


    Wpc = Mco2 * (h8 - h7)  # Precomp work input


    Wc = Mco2 * (h2 - h1)  # Compressor work input


    E_cycle = (Wt - Wc - Wpc) / (Mco2 * (h5 - h4))  # Cycle efficiency

    t5_values_plot.append(t5 - 273)
    E_cycle_values.append(E_cycle*100)

#plotting E_cycle vs TIT

plt.figure(figsize=(8, 6))
plt.plot(t5_values_plot, E_cycle_values, marker='o', linestyle='-', color='b')
plt.xlabel('Turbine Inlet Temperature (°C)')
plt.ylabel('Cycle Efficiency (%)')
plt.grid(True)
plt.title('Variation of Cycle Efficiency with Turbine Inlet Temperature (t5)')
plt.show()



#Parametric Study
p5_values = np.linspace(200*100000, 300*100000, 10)

p5_values_plot = []
E_cycle_values = []

for p5 in p5_values:
    Wt = 100 * 1000000  # Turbine work output

    Et = 0.9  # Turbine efficiency
    Ec = 0.85  # Compressor efficiency
    Epc = 0.85  # Precomp efficiency


    p6 = 90 * 100000  # Turbine outlet pressure
    p8 = 120 * 100000  # Precomp outlet pressure
    p10 = 1.36 * 100000  # Cooler inlet pressure
    p11 = 1.36 * 100000  # Cooler outlet pressure

    t5 = 560 +273   #TIT
    t10 = 20 + 273  # Cooler inlet temp
    t11 = 30 + 273  # Cooler outlet temp
    t1 = 35 + 273  # Compressor inlet temp
    t3 = 264 + 273  # Cold HTR inlet temp
    effec_HTR = 0.8  # effectiveness of HTR
    w_fluid = 'CO2'  # Working Fluid - CO2
    c_fluid = 'Water'  # Cooling Fluid - Water

    # PRESSURES
    Rt = p6 / p5


    p7 = p6
    Rpc = p8 / p7


    p9 = p8
    p1 = p9

    p4 = p5
    p3 = p4
    p2 = p3

    Rc = p2 / p1


    # Known enthalpies and entropies

    # Stream 5
    h5 = CP.PropsSI('H', 'P', p5, 'T', t5, w_fluid)
    s5 = CP.PropsSI('S', 'P', p5, 'T', t5, w_fluid)


    # Stream 3
    h3 = CP.PropsSI('H', 'P', p3, 'T', t3, w_fluid)
    s3 = CP.PropsSI('S', 'P', p3, 'T', t3, w_fluid)


    # Stream 1
    h1 = CP.PropsSI('H', 'P', p1, 'T', t1, w_fluid)
    s1 = CP.PropsSI('S', 'P', p1, 'T', t1, w_fluid)


    # Stream 10
    h10 = CP.PropsSI('H', 'P', p10, 'T', t10, c_fluid)
    s10 = CP.PropsSI('S', 'P', p10, 'T', t10, c_fluid)


    # Stream 11
    h11 = CP.PropsSI('H', 'P', p11, 'T', t11, c_fluid)
    s11 = CP.PropsSI('S', 'P', p11, 'T', t11, c_fluid)


    # TURBINE
    h6s = CP.PropsSI('H', 'P', p6, 'S', s5, w_fluid)
    h6 = h5 - (Et * (h5 - h6s))
    t6 = CP.PropsSI('T', 'P', p6, 'H', h6, w_fluid)
    s6 = CP.PropsSI('S', 'P', p6, 'T', t6, w_fluid)


    Mco2 = Wt / (h5 - h6)


    # HTR
    h_t3_p6 = CP.PropsSI('H', 'P', p6, 'T', t3, w_fluid)

    h7 = h6 - (effec_HTR * (h6 - h_t3_p6))

    t7 = CP.PropsSI('T', 'P', p7, 'H', h7, w_fluid)
    s7 = CP.PropsSI('S', 'P', p7, 'T', t7, w_fluid)


    h4 = h3 + (h6 - h7)

    t4 = CP.PropsSI('T', 'P', p4, 'H', h4, w_fluid)
    s4 = CP.PropsSI('S', 'P', p4, 'T', t4, w_fluid)


    # Precompressor
    h8s = CP.PropsSI('H', 'P', p8, 'S', s7, w_fluid)
    h8 = ((h8s - h7) / Epc) + h7

    t8 = CP.PropsSI('T', 'P', p8, 'H', h8, w_fluid)
    s8 = CP.PropsSI('S', 'P', p8, 'T', t8, w_fluid)

    # Compressor
    h2s = CP.PropsSI('H', 'P', p2, 'S', s1, w_fluid)
    h2 = ((h2s - h1) / Ec) + h1

    t2 = CP.PropsSI('T', 'P', p2, 'H', h2, w_fluid)
    s2 = CP.PropsSI('S', 'P', p2, 'T', t2, w_fluid)


    # LTR
    h9 = h8 - (h3 - h2)

    t9 = CP.PropsSI('T', 'P', p9, 'H', h9, w_fluid)
    s9 = CP.PropsSI('S', 'P', p9, 'T', t9, w_fluid)

    # Stream 9


    # Cooler
    Mwater = Mco2 * (h9 - h1) / (h11 - h10)


    Wpc = Mco2 * (h8 - h7)  # Precomp work input


    Wc = Mco2 * (h2 - h1)  # Compressor work input


    E_cycle = (Wt - Wc - Wpc) / (Mco2 * (h5 - h4))  # Cycle efficiency

    p5_values_plot.append(p5/100000)
    E_cycle_values.append(E_cycle*100)

#plotting E_cycle vs turbine inlet pressure

plt.figure(figsize=(8, 6))
plt.plot(p5_values_plot, E_cycle_values, marker='o', linestyle='-', color='b')
plt.xlabel('Turbine Inlet Pressure (bar)')
plt.ylabel('Cycle Efficiency (%)')
plt.grid(True)
plt.title('Variation of Cycle Efficiency with Turbine Inlet Pressure (p5)')
plt.show()

