from djitellopy import Tello
import time

dt = 0.05
Kp_roll = 1
Ki_roll = 0
Kd_roll = 0

Kp_pitch = 1
Ki_pitch = 0
Kd_pitch = 0


prev_error_ = 0

def PID_hoverX(current_speed, setpoint):
    error = current_speed - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp_roll * error + Ki_roll * e_int + Kd_roll * e_dot
    prev_error = error
    return speed_out

def PID_hoverZ(setpoint):
    error = Tello.get_speed_y() - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp_pitch * error + Ki_pitch * e_int + Kd_pitch * e_dot
    prev_error = error
    return speed_out

