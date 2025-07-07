from djitellopy import Tello
import connection as con
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

dt = 0.25
interrupted = False
accX_analysis = []
accY_analysis = []
time_stamps = []

saber = Tello()

if not con.connect_with_retry(saber):
    print('connection failed. program stoppped')
    sys.exit(1)

begin = time.time()
next_fetch = time.monotonic()
try:
    while True:
        now = time.monotonic()
        if now >= next_fetch:
            accX = saber.get_acceleration_x()
            accY = saber.get_acceleration_y()
            accX_analysis.append(accX)
            accY_analysis.append(accY)
            time_stamps.append(time.time() - begin)
            print(f'accX = {accX}\naccY = {accY}\n\n')
            next_fetch += dt 

except KeyboardInterrupt:
    if len(accX_analysis > 0 and accY_analysis > 0):

        print(f'program stopped by user')
        plt.figure()
    
        plt.subplot(1,2,1)
        plt.grid()
        plt.title('x acceleration')
        plt.plot(t, accX_analysis)
    
        plt.subplot(1,2,2)
        plt.grid()
        plt.title('y acceleration')
        plt.plot(t, accY_analysis)
        
        plt.show()
    else:
        print('no data collected]n')
    

except Exception as e:
    print(f'something wrong')
    # saber.land()

finally:
    saber.end()

        