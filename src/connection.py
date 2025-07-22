from djitellopy import Tello
import time

def connect_with_retry(tello, max_attempts=3):
    for attempt in range (max_attempts):
        try:
            # connect
            tello.connect()

            # get battery
            battery = tello.get_battery()
            print(f"Udah nyambung coy! Baterai = {battery}%")
        
            if battery <= 20:
                print(f"lowbat wak")
                return True
            return True
        
        except Exception as e:

            if attempt < max_attempts-1:
                print('reconnecting')
                time.sleep(3)
            else:
                print('connection timeout')
                return False
        return False






