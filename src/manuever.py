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

pid_state = {
    'roll': {'prev_error': 0, 'e_int': 0},
    'pitch': {'prev_error': 0, 'e_int': 0}
}

def PID_hoverX(speedX, setpoint=0):
    error = speedX - setpoint
    pid = pid_state['roll']
    pid['e_int'] += (pid['prev_error'] + error) / 2 * dt
    e_dot = (error - pid['prev_error']) / dt
    speed_out = Kp_roll * error + Ki_roll * pid['e_int'] + Kd_roll * e_dot
    pid['prev_error'] = error
    return speed_out

def PID_hoverY(speedY, setpoint=0):
    error = speedY - setpoint
    pid = pid_state['pitch']
    pid['e_int'] += (pid['prev_error'] + error) / 2 * dt
    e_dot = (error - pid['prev_error']) / dt
    speed_out = Kp_roll * error + Ki_roll * pid['e_int'] + Kd_roll * e_dot
    pid['prev_error'] = error
    return speed_out    

def hover(drone):
    drone.send_rc_control(PID_hoverX(drone), PID_hoverY(drone), 0, 0)

def stop(drone):
    drone.send_rc_control(0,0,0,0)

def go_forward(drone, fwd_speed, time):
    drone.send_rc_control(PID_hoverX(drone), fwd_speed, 0, 0)
    time.sleep(time)
    stop(drone)

def go_backward(drone, bck_speed, time):
    drone.send_rc_control(PID_hoverX(drone), -bck_speed, 0, 0)
    time.sleep(time)
    stop(drone)

def go_right(drone, r_speed, time):
    drone.send_rc_control(r_speed, PID_hoverY(drone), 0, 0)
    time.sleep(time)
    stop(drone)

def go_left(drone, l_speed, time):
    drone.send_rc_control(-l_speed, PID_hoverY(drone), 0, 0)
    time.sleep(time)
    stop(drone)

def go_right(drone, r_speed, time):
    drone.send_rc_control(r_speed, PID_hoverY(), 0, 0)
    time.sleep(time)
    stop(drone)

def go_left(drone, l_speed, time):
    drone.send_rc_control(-l_speed, PID_hoverY(), 0, 0)
    time.sleep(time)
    stop(drone)
    
