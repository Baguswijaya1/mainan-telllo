from djitellopy import Tello
import time

dt = 0.05

# PID components
Kp_roll = 1
Ki_roll = 0
Kd_roll = 0

Kp_pitch = 1
Ki_pitch = 0
Kd_pitch = 0

prev_error_ = 0

def PID_hoverX(setpoint=0):
    error = Tello.get_speed_x() - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp_roll * error + Ki_roll * e_int + Kd_roll * e_dot
    prev_error = error
    return speed_out

def PID_hoverY(setpoint):
    error = Tello.get_speed_y() - setpoint
    e_int = e_int + (prev_error + error)/2*dt
    e_dot = (error + prev_error)/dt
    speed_out = Kp_pitch * error + Ki_pitch * e_int + Kd_pitch * e_dot
    prev_error = error
    return speed_out

def hover(drone):
    drone.send_rc_control(PID_hoverX(), PID_hoverY(), 0, 0)
    
def go_forward(drone, fwd_speed)
    drone.send_rc_control(PID_hoverX(), fwd_speed, 0, 0)

def go_backward(drone, bck_speed):
    drone.send_rc_control(PID_hoverX(), -bck_speed, 0, 0)

def go_right(drone, r_speed):
    drone.send_rc_control(r_speed, PID_hoverY(), 0, 0)

def go_left(drone, l_speed):
    drone.send_rc_control(-l_speed, PID_hoverY(), 0, 0)

    
