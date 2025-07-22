from djitellopy import Tello
import connection, acquitition, manuever
import time
import sys

# create tello object
tello = Tello()

# Set timeout yang lebih panjang
tello.RESPONSE_TIMEOUT = 10  # 10 detik timeout

# connect to the drone with retry
can_connect = connection.connect_with_retry(tello)
if not can_connect:
    print("cannot connect to drone. program terminated")
    sys.exit(1)

# take off, wait, land
start_in = input('start? (y/n): ')
if start_in == "y":
    try:
        print("Takeoff...")
        tello.takeoff()
        time.sleep(3)  # Wait untuk stabilisasi
        
        print("Moving forward...")
        tello.send_rc_control(0, 30, 0, 0)
        # manuever.go_forward(tello, 30)
        time.sleep(4)
        tello.send_rc_control(0,0,0,0)
        time.sleep(0.5)

        print("moving backward")
        tello.send_rc_control(0,-20, 0, 0)
        time.sleep(4)
        tello.send_rc_control(0,0,0,0)
        time.sleep(0.5)

        print("yaw")
        tello.send_rc_control(0,0,0,40)
        time.sleep(3)
        tello.send_rc_control(0,0,0,0)
        time.sleep(1)

        print("go forward")
        tello.send_rc_control(0, 30, 0, 0)
        time.sleep(4)
        tello.send_rc_control(0,0,0,0)
        time.sleep(0.5)
        
        print("Landing...")
        tello.land()
        print("Flight completed successfully!")
        start_in = "n"
    
    except Exception as e:
        print(f"Error during flight: {e}")
        print("Attempting emergency landing...")
        try:
            tello.land()
        except:
            print("Emergency landing failed!")

        # close connection
        print("Closing connection...")
        tello.end()
    
