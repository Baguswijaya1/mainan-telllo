from djitellopy import Tello
import numpy as np
import time

drone = Tello()
drone.get_spe

def speed_stream(drone, freq):
    now = time.monotonic()
    next = time.monotonic()
    dt = 1/freq
    if now == next:
        speed_x = drone.get_speed

def accel_filter(current_accel, raw_data):
    raw_data.append(current_accel)
    if len(raw_data) == 5:
        filtered_data =  np.average(raw_data)
        raw_data = []
        return filtered_data

def filter_time_stemp(current_time, begin_time):
    return current_time - begin_time

def kalman():
    pass

