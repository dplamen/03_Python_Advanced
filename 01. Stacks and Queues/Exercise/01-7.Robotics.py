from collections import deque
import datetime

robots = [[name, int(speed), 0] for name, speed in [x.split("-") for x in input().split(";")]]
starting_time = datetime.datetime.strptime(input(), "%H:%M:%S")
products = deque()

command = input()
while not command == "End":
    products.append(command)
    command = input()

sec = 0
while products:
    sec += 1
    for robot_index in range(len(robots)):
        robot, speed, start_time = robots[robot_index]
        if start_time <= sec:
            robots[robot_index][2] = sec + speed
            print(f"{robot} - {products.popleft()} [{(starting_time + datetime.timedelta(seconds=sec)).time()}]")
            break
    else:
        products.rotate(-1)