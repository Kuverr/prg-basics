###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > 140:
    print(f'Your speed is {...}km/h')
    print('Warning: speed limit exceeded!!')