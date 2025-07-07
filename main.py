from djitellopy import Tello
import hover
import connection as con
import sys
import time

dt = 0.1

saber = Tello()

if not con.connect_with_retry(saber):
    print('connection failed. program stoppped')
    sys.exit(1)

try:
    while True:
        start_time = int(round(time.time()))
        speedX = saber.get_speed_x()
        speedY = saber.get_speed_y()
        speedZ = saber.get_speed_z()

        print(f'speed x : {speedX}\nspeed y : {speedY}\nspeed z : {speedZ}\n')

        # sleep
        elapsed_time = time.time - start_time
        

except KeyboardInterrupt:
    print(f'program stopped by user')

finally:
    saber.end()

        