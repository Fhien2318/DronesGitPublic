from pioneer_sdk import Pioneer
from math import pi
from time import sleep

drone = Pioneer()

p = pi



try:

        start_point = [0, 0, 1, 0, 0, 1]

        coordinates = [start_point,
                       [0, 1, 0, 0, 1, 1],
                       [0, 0, 0, 0.5 * p, 1, 0],
                       [0, 1, 0, 0, 1, 1],
                       [0, 0, 0, 0.5 * p, 1, 0],
                       [0, 1, 0, 0, 1, 1],
                       [0, 0, 0, 0.5 * p, 1, 0],
                       [0, 1, 0, 0, 1, 1],
                       [0, 0, 0, 0.5 * p, 1, 0],
                       start_point]
        
        colors = [[255, 1, 0, 0],
                  [255, 1, 0.2, 0],
                  [255, 1, 0.5, 0],
                  [255, 0, 1, 0],
                  [255, 0.2, 0.2, 1]]

        color = 0

        drone.arm()

        sleep(1)

        drone.takeoff()
        input()

        for num in range(len(coordinates)):
            if coordinates[num][4] == 0:
                drone.go_to_local_point(*coordinates[num][0:4])
            elif coordinates[num][4] == 1:
                drone.go_to_local_point_body_fixed(*coordinates[num][0:4])
            while not drone.point_reached():
                pass
            if coordinates[num][5] == 1:
                drone.led_control(*colors[color])
                color += 1

finally:
    
    drone.led_control(255, 0, 0, 0)
    drone.land()