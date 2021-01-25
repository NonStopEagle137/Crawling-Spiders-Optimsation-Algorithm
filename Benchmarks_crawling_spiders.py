# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:16:14 2020

@author: Athrva Pandhare
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:36:04 2020

@author: Athrva Pandhare
"""

## Crawling Spiders Optimisation Technique Author : Athrva Pandhare
from cec17_functions import cec17_test_func
#import ctypes
#ctypes.windll.LoadLibrary("C:/Users/Athrva Pandhare/Desktop/CEC2017/cec17_python-master/cec17_test_func.dll")

import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(1040)
func = []
def prob_calc(func_ini, func_curr, temperature):
    prob = 1/(np.exp((func_curr-func_ini)/temperature))
    
    return prob

'''
def obj_calc(x,obj): ## Schaffer n4
    global func
    obj = []
    for i in range(len(x)):
        numeratorcomp = (np.cos(np.sin(abs(x[i][0]** 2 - x[i][1]** 2)))** 2) - 0.5; 
        denominatorcomp = (1 + 0.001 * (x[i][0]**2 + x[i][1]**2))**2 ;
        obj.append(100*(0.5 + (numeratorcomp/ denominatorcomp)));  
        func.append(1000*(0.5 + (numeratorcomp/ denominatorcomp)))

    
    return obj
'''
'''
def obj_calc(x,obj):   #f1
    global func
    obj = []
    for i in range(len(x)):
        z = 25
        for j in range(5):
            z += np.floor(x[i][j])
        obj.append(z)
        func.append(z)
    return obj
'''
'''
def obj_calc(x_p, obj):
    obj = []
    for i in range(0, len(x_p)):
        obj.append(x_p[i][0]**2 +x_p[i][1]**2)
    return obj
'''
def check():
    nx = 10
    # mx: Number of objective functions
    mx = 1
    # func_num: Function number
    func_num = 3
    val = [0]
    val2 = [0]
    x_p = [0.0000000000000000e+00   ,2.7190935589964482e-01   ,0.0000000000000000e+00   ,0.0000000000000000e+00  , 0.0000000000000000e+00  , 0.0000000000000000e+00   ,0.0000000000000000e+00  , 4.7391519609448363e-01 , -8.3753787322423090e-01 ,  0.0000000000000000e+00]
    cec17_test_func(x_p, val, nx, mx, func_num)
    your = [-5.614352456656413892e+01,4.671086713798583645e+00,3.533073592580392841e+01,8.105778579744983503e+00,-4.743617194900124900e+01,7.262462375852702046e+00,6.578025615142204963e+00,-2.671261856681210745e+00,-6.112518844107479055e+01,-4.698942056219460284e+01]

    cec17_test_func(your, val2, nx, mx, func_num)
    if val2< val:
        print("Current Best")
    else:
        print("Optimisation Failed")
    print(val)
    print(val2)
    return val2
#def learning_schedule(t):
#    return t0/(t + t1)
    

def motion():

    # nx: Number of dimensions
    nx = 10
    # mx: Number of objective functions
    mx = 1
    # func_num: Function number
    func_num = 9
    lower = -100 # Defining the constraints
    upper = 100
    polarity = [];
    iterations = 90;
    visual = [];
    points = [];

    dim = nx;
    val = []
    obj = []
    c1 = []
    c2 = []
    
    for i in range(100):
        val.append([0])
        obj.append(0)
        polarity.append(1)
    x_p = np.zeros(100*dim).reshape(100,dim);

    for i in range(len(x_p)):
        for j in range(dim):
            x_p[i][j] = x_p[i][j] + random.uniform(lower,upper)
        cec17_test_func(x_p[i], val[i], nx, mx, func_num)
        points.append(x_p[i])
        obj[i] = val[i][0]
        visual.append(val[i][0])
        var = [0];
        var1= [0];
    x_p[0] = points[visual.index(float(min(visual)))]
    for j in range(iterations):
        print(" Iteration Number", j)
        print("------------------------------")
        fixed = points[visual.index(float(min(visual)))]
        
        x_p[0] = fixed
        #print(fixed)
        for i in range(len(x_p)):
            #fixed = points[visual.index(float(min(visual)))]
            if np.average(x_p[i]) != np.average(fixed):
            #y1.append(((x_p[i][1]-fixed[1])/(x_p[i][0]- fixed[0]))*x_cords[i])
                for j in range(dim):
                    #print("running")
                    x_p[i][j] = ((x_p[i][j]+fixed[j])/2) + random.uniform(-0.9,0.9) 
            for i1 in range(15):
                temp = fixed
                temp = temp + random.uniform(random.uniform(-0.9,0.9),random.uniform(-0.9,0.9))
                cec17_test_func(temp, var, nx, mx, func_num)
                cec17_test_func(fixed, var1, nx, mx, func_num)
                if var < var1:
                    print(temp)
                    visual.append(var[0])
                    #c2.append(temp)
                    points.append(temp)
                    fixed = points[visual.index(float(min(visual)))]
                    x_p[0] = fixed
            cec17_test_func(x_p[i], val[i], nx, mx, func_num)
            points.append(x_p[i])
            obj[i] = val[i][0]
            visual.append(val[i][0])
    # Solution Smoothening Sweeps
    print(" Starting Smoothening Sweeps")
    for i1 in range(9500):
        temp = fixed
        temp = temp + random.uniform(-0.009,0.009)
        cec17_test_func(temp, var, nx, mx, func_num)
        cec17_test_func(fixed, var1, nx, mx, func_num)
        if var < var1:
            print(temp)
            visual.append(var[0])
            #c2.append(temp)
            points.append(temp)
            fixed = points[visual.index(float(min(visual)))]
    
    return [fixed, float(min(visual)),visual,temp,c1,c2]
def simulated(fixed):
        ### Parameters for Simulated Annealing
    m = 350; # Outer Iterations
    n = 37; # inner iterations
    alpha = 0.9;
    temperature = 1000; # defining the initial temperature
    interval = 0.9; # Defining fixed interval for traversing
    temper = []
    func2 = [0]
    func = [0]
    func_ini = []
    func_curr = []
    evaluation_point = []
    points= []
    nx = 10
    # mx: Number of objective functions
    mx = 1
    # func_num: Function number
    func_num = 6
    fixed_sim = np.zeros(len(fixed))
    for i in range(m):     # Outer Iterations
        temper.append(temperature)
        cec17_test_func(fixed, func, nx, mx, func_num)
        #func = func_eval(x,y)
        if i == 0 :
            func_ini.append(func)
            points.append(fixed)
        else:
            temperature = alpha * temperature
            func_ini.append(func)

        for j in range(n): # inner iterations for neighbourhood
            for i in range(len(fixed)):
                fixed_sim[i] = fixed[i] - random.uniform(-interval, interval)
            #y_curr = y - random.uniform(-interval, interval)
            cec17_test_func(fixed_sim, func2, nx, mx, func_num)
            func_curr.append(func2)
            #stru = [x_curr, y_curr]
            evaluation_point.append(fixed_sim)
            
            if func_curr[j] > func:
                prob = prob_calc(func[0], func_curr[-1][0], temperature)
                r = random.uniform(0.3,1)  # Probability for checking
                if r> prob:
                    func = func_curr[func_curr.index(min(func_curr))]
                    fixed = evaluation_point[func_curr.index(min(func_curr))]
                    #y = evaluation_point[func_curr.index(min(func_curr))][1]
            else :
                func = func_curr[func_curr.index(min(func_curr))]
                fixed = evaluation_point[func_curr.index(min(func_curr))]
                #y = evaluation_point[func_curr.index(min(func_curr))][1]
    

    return [fixed]
'''
        for i in range(len(x_p)):
            
            fixed = points[visual.index(float(min(visual)))]
            
            x_p[0] = fixed # previous iteration's best value
            #cec17_test_func(fixed, var, nx, mx, func_num)
            #cec17_test_func(temp, var1, nx, mx, func_num)
            #for i in range(0,5):
            temp = fixed
            for j in range(len(fixed)):
                if fixed[j] > 0:
                    fixed[j] = fixed[j] + polarity[j]* random.uniform(-0.7,0.7)
                else:
                    fixed[j] = -1*(abs(fixed[j]) + polarity[j]*random.uniform(-0.7,0.7))
                    cec17_test_func(fixed, var, nx, mx, func_num)
                    cec17_test_func(temp, var1, nx, mx, func_num)
                    if var1 < var:
                        fixed = temp
                        polarity[j] = -1*polarity[j]
'''
                        
            

answer = motion()
plt.plot(range(len(answer[2])),answer[2])
'''Optima = [0]
fixed = answer[0]
ha = [0]
hu = [46.765665, 42.816892, 6.28015333, 64.0107, 43.92423, 30.8041, -35.6648, -91.4081, 43.18139,60.394861]
check = cec17_test_func(hu,ha, 10, 1, 6)
nx = 10
#mx: Number of objective functions
mx = 1
#func_num: Function number
func_num = 6
final = simulated(fixed)  
cec17_test_func(final[0], Optima, nx, mx, func_num) 
sol = [];
c1 = []
for j in range(len(answer[-1])):
    c1.append([0])
for i in range(len(answer[-1])):
    cec17_test_func(answer[-1][i],c1[i], 10, 1, 6)
    sol = c1[i][0]

'''
     

    
    
    