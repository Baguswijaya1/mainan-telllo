import numpy as np
import time

def speed_stream(master, freq):
    now = time.monotonic()




def accel_filter(current_accel, raw_data):
    raw_data.append(current_accel)
    if len(raw_data) == 5:
        filtered_data =  np.average(raw_data)
        raw_data = []
        return filtered_data

def filter_time_stemp(current_time, begin_time):
    return current_time - begin_time