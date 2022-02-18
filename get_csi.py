import sys
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

# Create figure for plotting
plt.close('all')
plt.figure()
plt.ion()
plt.show()

def process(res):
    # print("res",res)
    all_data = res.split(',')
    # print(all_data[25])
    csi_data = all_data[25].split(" ")
    csi_data[0] = csi_data[0].replace("[", "")
    csi_data[-1] = csi_data[-1].replace("]", "") 
    csi_data.pop()
    csi_data = [int(c) for c in csi_data if c]
    # print(csi_data)    
    imaginary = []
    real = []
    for i, val in enumerate(csi_data):
        if i % 2 == 0:
            imaginary.append(val)
        else:
            real.append(val)
    
    print(imaginary)
    print(real)
    # print("real", len(real))
    csi_size = 128
    x = []
    y = []
    amplitudes = []
    phases = []
    csi = []
    if len(imaginary) > 0 and len(real) > 0:
        for j in range(int(csi_size / 2)):  
            amplitudeCalc = math.sqrt(imaginary[j] ** 2 + real[j] ** 2)
            phaseCalc = math.atan2(imaginary[j], real[j])  
            amplitudes.append(amplitudeCalc)
            phases.append(phaseCalc)
            x.append(j)

        y = csi
        print("x:", x)
        print("y:", y)
        plt.cla()
        plt.plot(x,y)
        plt.pause(0.0001)

while True:
    line = sys.stdin.readline()
    if "CSI_DATA" in line:
        process(line)

