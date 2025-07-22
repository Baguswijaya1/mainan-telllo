from djitellopy import Tello
import connection as con
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import acquitition

dt = 0.25
accX_analysis = []
accY_analysis = []
spdX_analysis = []
spdY_analysis = []
time_stamps = []  # Store actual timestamps
raw_data = []

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
            current_time = time.time()
            accX = saber.get_acceleration_x()
            accY = saber.get_acceleration_y()
            spdX = saber.get_speed_x()
            spdY = saber.get_speed_y()
            
            # # apply moving average filter
            # accFil_x = acquitition.accel_filter(accX, raw_data)
            # accFil_y = acquitition.accel_filter(accY, raw_data)
            # temp = saber.get_temperature()          
            # if accFil_x is not None and accFil_y is not None:
            #     time_stamps.append(current_time - begin)  
            #     accX_analysis.append(accFil_x)
            #     accY_analysis.append(accFil_y)
            #     print(f'accX = {accFil_x}\naccY = {accFil_y}\ntemperature = {temp}\n')

            # fetch without filter
            accX_analysis.append(accX)
            accY_analysis.append(accY)
            spdX_analysis.append(spdX)
            spdY_analysis.append(spdY)
            time_stamps.append(current_time - begin)  
            temp = saber.get_temperature()
            print(f'accX = {accX}\naccY = {accY}\ntemperature = {temp}')
            print(f'spdX = {spdX}\nspdY = {spdY}\n')
            

            next_fetch += dt 

except KeyboardInterrupt:
    print(f'program stopped by user')
    
    # Check if we have data to plot
    if len(accX_analysis) > 0 and len(time_stamps) > 0:
        plt.figure(figsize=(12, 5))

        plt.subplot(2,2,1)
        plt.grid()
        plt.title('X Acceleration vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Acceleration (cm/s²)')
        plt.plot(time_stamps, accX_analysis, 'b.-')

        plt.subplot(2,2,2)
        plt.grid()
        plt.title('Y Acceleration vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Acceleration (cm/s²)')
        plt.plot(time_stamps, accY_analysis, 'r.-')
        
        plt.subplot(2,2,3)
        plt.grid()
        plt.title('x speed vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('speed (cm/s)')
        plt.plot(time_stamps, spdX_analysis, 'r.-')
        
        plt.subplot(2,2,4)
        plt.grid()
        plt.title('y speed vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('speed (cm/s)')
        plt.plot(time_stamps, spdY_analysis, 'r.-')

        plt.tight_layout()
        plt.show()
        
        print(f"Data collected for {time_stamps[-1]:.2f} seconds")
        print(f"Total data points: {len(accX_analysis)}")
    else:
        print("No data collected to plot")

except Exception as e:
    print(f'something wrong: {e}')
    # saber.land()

finally:
    saber.end()

