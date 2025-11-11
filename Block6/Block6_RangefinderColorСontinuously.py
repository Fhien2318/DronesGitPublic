from pioneer_sdk import Pioneer
from math import pi
from time import sleep

drone = Pioneer()

p = pi



try:

    color = -1
    while True:
        a = drone.get_dist_sensor_data(get_last_received=True)
        if a != None:
            if a < 0.1 and color != 0:
                drone.led_control(255, 1, 0, 0)
                color = 0
            if a > 1.1 and color != 1:
                drone.led_control(255, 0, 1, 0)
                color = 1
            if 0.1 <= a <= 1.1:
                drone.led_control(255, 1.1 - a, a - 0.1, 0)
                color = 2

finally:
    
    drone.led_control(255, 0, 0, 0)
    drone.land()