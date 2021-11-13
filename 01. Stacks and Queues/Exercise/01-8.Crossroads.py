from collections import deque

green = int(input())
window = int(input())

cars = deque()
cars_passed = 0
crashed = False

command = input()
while command != 'END':
    if command == 'green':
        green_time = green
        while cars:
            current_car = cars.popleft()
            if len(current_car) > green_time + window:
                crashed = True
                print(f'A crash happened!')
                hit = current_car[green_time + window]
                print(f'{current_car} was hit at {hit}.')
                break
            elif len(current_car) >= green_time:
                cars_passed += 1
                break
            else:
                cars_passed += 1
                green_time -= len(current_car)
                continue
    else:
        cars.append(command)
    if crashed:
        break

    command = input()

if not crashed:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')


