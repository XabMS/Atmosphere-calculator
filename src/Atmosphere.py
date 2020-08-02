from math import sqrt

#alturas
h=[0, 11000, 20000, 32000, 47000, 51000, 71000, 84852]
a=[-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002]
P=[101325,0,0,0,0,0,0,0]
rho=[1.225,0,0,0,0,0,0]
T=[288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.95]

#Ctes
g = 9.80665
R = 287
e = 2.718

last= 0

print("Insert altitude (m, máximo 84850):")
altura = int(input())

#calculos
for i in range(7):
    if h[i+1] > altura:
        last = 1
    
    if last == 1:    
        if a[i] == 0:
            P = P[i] * e**((-g/(R*T[i]))*(altura-h[i]))
            rho = rho[i] * e**((-g/(R*T[i]))*(altura-h[i]))
            T2 = T[i]
        else:
            T2 = T[i]+ (altura-h[i])*a[i]
            P = P[i] * (T2/T[i])**(-g/(a[i]*R))
            rho = rho[i] * (T2/T[i])**((-g/(a[i]*R))-1)
        break
            
    else:
        if a[i] == 0:
            P[i+1] = P[i] * e**((-g/(R*T[i]))*(h[i+1]-h[i]))
            rho[i+1] = rho[i] * e**((-g/(R*T[i]))*(h[i+1]-h[i]))
        else:
            T2 = T[i]+ (h[i+1]-h[i])*a[i]
            P[i+1] = P[i] * (T2/T[i])**(-g/(a[i]*R))
            rho[i+1] = rho[i] * (T2/T[i])**((-g/(a[i]*R))-1)
        
M = sqrt((1.4*P)/rho)

print("For " + str(altura) + "m altitude:")
print("Temperature: " + str(T2) +"K (" + (str(T2-273.15) + " C)"))
print("Pressure: " + str(P) + "Pa (" + str(P/101325) +"%)")
print("Density: " + str(rho) + "Kg/m3 (" + str(rho/1.225) +"%)")
print("Speed of sound: " + str(M) + "m/s (" + str(M*3.6) + "km/h)")
