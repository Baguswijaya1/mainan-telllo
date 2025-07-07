from djitellopy import Tello
import connection as con
import sys
import time

dt = 0.25
interrupted = False
accX_analysis = []
accY_analysis = []

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
            print(f'accX = {accX}\naccY = {accY}\n\n')
            next_fetch += dt 

except KeyboardInterrupt:
    print(f'program stopped by user')   
    

except Exception as e:
    print(f'something wrong')
    # saber.land()

finally:
    saber.end()

        