from pioneer_sdk import Pioneer
from math import pi
from time import sleep

drone = Pioneer()

p = pi



try:

        drone.arm()
        sleep(1)
        drone.takeoff()

        drone.go_to_local_point_body_fixed(0, 0, 1.5, 0)  
        while not drone.point_reached():
            pass

        colors = [[255, 1, 0, 0],
                  [255, 1, 0.2, 0],
                  [255, 1, 0.5, 0],
                  [255, 0, 1, 0],
                  [255, 0.2, 0.2, 1],
                  [255, 0, 0, 1],
                  [255, 1, 0, 1]]
        
        color = 0
        
        drone.led_control(255, 0, 0, 0)
        
        while True:
            if drone.get_dist_sensor_data(get_last_received=True) < 1:
                drone.led_control(*colors[color])
                color = (color + 1) % 7
                sleep(1)

finally:
    
    drone.led_control(255, 0, 0, 0)
    drone.land()