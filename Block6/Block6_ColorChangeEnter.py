from pioneer_sdk import Pioneer
from math import pi
from time import sleep

drone = Pioneer()

p = pi



try:

    while True:
        input()
        drone.led_control(255, 1, 0, 0)

        input()
        drone.led_control(255, 1, 0.2, 0)

        input()
        drone.led_control(255, 1, 0.5, 0)

        input()
        drone.led_control(255, 0, 1, 0)

        input()
        drone.led_control(255, 0.2, 0.2, 1)

        input()
        drone.led_control(255, 0, 0, 1)

        input()
        drone.led_control(255, 1, 0, 1)


finally:
    
    drone.led_control(255, 0, 0, 0)
    drone.land()