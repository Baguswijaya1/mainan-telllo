from djitellopy import Tello
import connection as con
import sys
import time
import numpy as np
import matplotlib.pyplot as plt

dt = 0.25
accX_analysis = []
accY_analysis = []
time_stamps = []  # Store actual timestamps

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
            
            accX_analysis.append(accX)
            accY_analysis.append(accY)
            time_stamps.append(current_time - begin)  # Relative time from start
            
            print(f'accX = {accX}\naccY = {accY}\n\n')
            next_fetch += dt 

except KeyboardInterrupt:
    print(f'program stopped by user')
    
    # Check if we have data to plot
    if len(accX_analysis) > 0 and len(time_stamps) > 0:
        plt.figure(figsize=(12, 5))

        plt.subplot(1,2,1)
        plt.grid()
        plt.title('X Acceleration vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Acceleration (cm/s²)')
        plt.plot(time_stamps, accX_analysis, 'b.-')

        plt.subplot(1,2,2)
        plt.grid()
        plt.title('Y Acceleration vs Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Acceleration (cm/s²)')
        plt.plot(time_stamps, accY_analysis, 'r.-')
        
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

