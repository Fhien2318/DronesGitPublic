from pioneer_sdk import Pioneer
from math import pi
from time import sleep

drone = Pioneer()

p = pi



try:

    while True:
        drone.led_control(255, 1, 1, 1)
        sleep(0.05)
        drone.led_control(255, 0, 0, 0)
        sleep(1)

finally:
    
    drone.led_control(255, 0, 0, 0)
    drone.land()