import math
import pandas as pd 


Qx = float(input('Normal Stress along X-dir Qx: '))
Qy = float(input('Normal Stress along Y-dir Qy: '))
Txy = float(input('Shear Stress Txy: '))

orientation_list = eval(input('Enter angles of orientation as a list: '))
E11 = int(input('E11: '))
E22 = int(input('E22: '))
G12 = int(input('G12: '))
y12 = float(input('y12: '))

print('Tsai-Wu Failure Theory Criteria')
Q1t = float(input('Q1t: '))
Q1c = float(input('Q1c: '))
Q2t = float(input('Q2t: '))
Q2c = float(input('Q2c: '))
t12 = float(input('t12: '))

Final_list = []
Fx_list = []
Fy_list = []
Vxy_list = []
F1_list = []
F2_list = []
V12_list = []
Q1_list = []
Q2_list = []
T12_list = []
TsaiWu_list = []



for i in range(len(orientation_list)):
    #angle = int(input("Fiber orientation: "))
    r_angle = orientation_list[i] * (math.pi / 180)
    sin = math.sin(r_angle)
    print('sin: ',sin)
    sin2 = math.sin(2 * r_angle)
    cos = math.cos(r_angle)
    print('cos: ',cos)
    cos2 = math.cos(2 * r_angle)
    print()
    print("Lamina calculation for {} radian".format(r_angle))
    Exx = 1 / ((((cos ** 4) / E11) + ((sin ** 4) / E22) + (0.25 * ((1/G12)-(2 * y12 / E11)) * (sin2 ** 2))))

    Eyy = 1 / ((((sin ** 4) / E11) + ((cos ** 4) / E22) + (0.25 * ((1/G12)-(2 * y12 / E11)) * (sin2 ** 2))))

    Gxy = 1 / ((1 / E11) + ((2 * y12) / E11) + (1 / E22) - (((1 / E11) + ((2 * y12) / E11) + (1 / E22) - (1 / G12)) * (cos2 ** 2)))
    print('Exx:',Exx)
    print('Eyy:',Eyy)
    print('Gxy:',Gxy)
    print('------------------------------------------------------------------------------')

    S11 = 1 / E11
    S12 = -(y12 / E11)
    S22 = 1 / E22
    S66 = 1 / G12
    y21 = - (S12/S22)

    print('S11:',S11) 
    print('S12:',S12)
    print('S22:',S22) 
    print('S66:',S66)
    print('y21:',y21)
    print('------------------------------------------------------------------------------')

    S11_ = (S11 * (cos ** 4)) + (((2 * S12) + S66) * (sin ** 2) * (cos ** 2)) + (S22 * (sin ** 4))
    
    S12_ = (S12 * ((sin ** 4) + (cos ** 4))) + ((S11 + S22 - S66) * (sin ** 2) * (cos ** 2))  
    
    S22_ = (S11 * (sin ** 4)) + (((2 * S12) + S66) * (sin ** 2) * (cos ** 2)) + (S22 * (cos ** 4))

    if S11 == S22 and (orientation_list[i] == 0 or 45 or 90):
    	S16_ = 0.0
    	S26_ = 0.0
    else:
    	S16_ = ((2 * S11 - 2 * S12 - S66) * sin * (cos ** 3)) - ((2 * S22 - 2 * S12 - S66) * (sin ** 3) * cos)
    	S26_ = ((2 * S11 - 2 * S12 - S66) * (sin ** 3) * cos) - ((2 * S22 - 2 * S12 - S66) * sin * (cos ** 3))
    
    S66_ = (2 * ((2 * S11) + (2 * S22) - (4 * S12) - S66) * (sin ** 2) * (cos ** 2)) + (S66 * ((sin ** 4)+(cos **4)))

    print('S11_:',S11_)
    print('S12_:',S12_)
    print('S22_:',S22_)
    print('S16_:',S16_)
    print('S26_:',S26_)
    print('S66_:',S66_)
    print('------------------------------------------------------------------------------')

    Fx = (S11_ * Qx) + (S12_ * Qy) + (S16_ * Txy)
    Fy = (S12_ * Qx) + (S22_ * Qy) + (S26_ * Txy)
    Vxy = (S16_ * Qx) + (S26_ * Qy) + (S66_ * Txy)

    print('GLOBAL VARIABLES')
    print('Fx: ',Fx)
    print('Fy: ',Fy)
    print('Vxy: ',Vxy)
    print('------------------------------------------------------------------------------')

    F1 = ((cos ** 2) * Fx) + ((sin ** 2) * Fy) + ((2 * sin * cos) * (Vxy / 2))
    F2 = ((sin ** 2) * Fx) + ((cos ** 2) * Fy) - ((2 * sin * cos) * (Vxy / 2))
    V12 = - ((sin * cos) * Fx) + ((sin * cos) * Fy) + (((cos ** 2) - (sin **2)) * (Vxy / 2)) 

    print('LOCAL STRAINS')
    print('F1: ',F1)
    print('F2: ',F2)
    print('V12/2 : ',V12)
    print('------------------------------------------------------------------------------')

    Q1 = ((cos ** 2) * Qx) + ((sin ** 2) * Qy) + ((2 * sin * cos) * Txy)
    Q2 = ((sin ** 2) * Qx) + ((cos ** 2) * Qy) - ((2 * sin * cos) * Txy)
    T12 = - ((sin * cos) * Qx) + ((sin * cos) * Qy) + (((cos ** 2) - (sin **2)) * Txy)

    print('LOCAL STRESSES')
    print('Q1: ',Q1)
    print('Q2: ',Q2)
    print('T12: ',T12)
    print('------------------------------------------------------------------------------')

    Qmax = ((Qx + Qy) / 2) + math.sqrt((((Qx - Qy) / 2) ** 2) + (Txy ** 2))
    Qmin = ((Qx + Qy) / 2) - math.sqrt((((Qx - Qy) / 2) ** 2) + (Txy ** 2))

    print('PRINCIPAl STRESSES')
    print('Maximum principal stress Qmax: ',Qmax)
    print('Minimum principal stress Qmin: ',Qmin)
    print('------------------------------------------------------------------------------')

    Op = 0.5 * math.atan((2 * Txy) / (Qx - Qy))

    print('The value of angle at which maximum normal stress occur')
    print('Op: ',(Op * (180 / math.pi)))
    print('------------------------------------------------------------------------------')

    Tmax = math.sqrt((((Qx - Qy) / 2) ** 2) + (Txy ** 2))

    print('Maximum Shear Stress Tmax: ',Tmax)
    print('------------------------------------------------------------------------------')


    Os = 0.5 * math.atan((Qy - Qx) / (2 * Txy))
    print('The value of angle at which maximum shear stress occur')
    print('Os: ',(Os * (180 / math.pi)))
    print('------------------------------------------------------------------------------')

    Fmax = ((Fx + Fy) / 2) + math.sqrt((((Fx - Fy) / 2) ** 2) + ((Vxy / 2) ** 2))
    Fmin = ((Fx + Fy) / 2) - math.sqrt((((Fx - Fy) / 2) ** 2) + ((Vxy / 2) ** 2))
    print('PRINCIPAl STRAINS')
    print('Maximum principal strain Fmax: ',Fmax)
    print('Minimum principal strain Fmin: ',Fmin)
    print('------------------------------------------------------------------------------')

    Oq = 0.5 * math.atan(Vxy / (Fx - Fy))

    print('The value of angle at which maximum normal stress occur')
    print('Op: ',(Oq * (180 / math.pi)))
    print('------------------------------------------------------------------------------')

    print('Tsai-Wu Failure Theory')

    H1 = (1 / Q1t) - (1 / Q1c)
    H11 = 1 / (Q1t * Q1c)
    H2 = (1 / Q2t) - (1 / Q2c)
    H22 = 1 / (Q2t * Q2c)
    H6 = 0
    H66 = 1 / (t12 ** 2)
    H12 = - (0.5 * math.sqrt(1 /(Q1t * Q1c * Q2t * Q2c )))

    print('H1: ',H1)
    print('H11: ',H11)
    print('H2: ',H2)
    print('H22: ',H22)
    print('H6: ',H6)
    print('H66: ',H66)
    print('H12: ',H12)


    Final = (H1 * Q1) + (H2 * Q2) + (H6 * T12) + (H11 * (Q1 ** 2)) + (H22 * (Q2 ** 2)) + (H66 * (T12 ** 2)) + (2 * H12 * Q1 * Q2)
    print('Tsai-Wu Value: ',Final)
    if Final < 1:
    	print("It hasn't violated the Tsai-Wu Criteria ")
    else: 
    	print("It has violated the Tsai-Wu Criteria")
    print('------------------------------------------------------------------------------')

    TsaiWu = Final < 1

    Final_list.append(Final)
    Fx_list.append(Fx)
    Fy_list.append(Fy)
    Vxy_list.append(Vxy)
    F1_list.append(F1)
    F2_list.append(F2)
    V12_list.append(V12)
    Q1_list.append(Q1)
    Q2_list.append(Q2)
    T12_list.append(T12)
    TsaiWu_list.append(TsaiWu)
#print(orientation_list)
#print(Fx_list)
#print(Fy_list)
#print(Vxy_list)
#print(F1_list)
#print(F2_list)
#print(V12_list)
#print(Q1_list)
#print(Q2_list)
#print(T12_list)
#print(TsaiWu_list)
print('------------------------------------------------------------------------------')
my_dict = {'angle':orientation_list, 'Fx':Fx_list, 'Fy':Fy_list, 'Vxy':Vxy_list, 'F1':F1_list, 'F2':F2_list, 'V12':V12_list, 'Q1':Q1_list, 'Q2':Q2_list, 'T12': T12_list, 'Tsai-Wu Criteria': TsaiWu_list}
table = pd.DataFrame(my_dict)
print('Calculation Table For Tsai-Wu Criteria')
print(table)
print('------------------------------------------------------------------------------')

def check(Final_list):
	return (all(x < 1 for x in Final_list))

if(check(Final_list)):
	print('All the laminas are obeying Tsai-Wu Criteria')
else:
	print('Some of the laminas are not obeying Tsai-Wu Criteria')










