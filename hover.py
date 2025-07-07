from djitellopy import Tello
import time

dt = 0.05
Kp = 1
Ki = 0
Kd = 0
prev_error = 0

def PID_hoverX(setpoint):
    error = Tello.get_speed_x() - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp * error + Ki * e_int + Kd * e_dot
    prev_error = error
    return speed_out

def PID_hoverZ(setpoint):
    error = Tello.get_speed_y() - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp * error + Ki * e_int + Kd * e_dot
    prev_error = error
    return speed_out

