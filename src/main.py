from djitellopy import Tello
import time
import connection, acquitition, manuever
import numpy as np

drone = Tello()
if not connection.connect_with_retry(drone):
    print("connection failed\n")

# timing system
now = time.monotonic()
next = time.monotonic()

while True:
    






