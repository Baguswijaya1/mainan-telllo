from djitellopy import Tello
import time

def connect_with_retry(tello, max_attempts=5):
    for attempt in range (max_attempts):
        try:
            # connect
            print(f'connecting Tello ({attempt + 1} / {max_attempts} attempts)')
            tello.connect()

            # get battery
            battery = tello.get_battery()
            print(f"Drone connected! Battery : {battery}%")

            # check minimum battery level
            if battery <= 15:
                print(f"Battery low, please charge\nBattery : {battery}%")
                return False
            return True
        
        except Exception as e:

            if attempt < max_attempts-1:
                print('reconnecting..')
                time.sleep(3)
            else:
                print('connection timeout')
                return False
    return False