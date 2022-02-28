# t = d / s

limit = input('Speed limit/ms^-1: ')
speed = input('Actual speed/ms^-1: ')
distance = input('Distance traveled/m: ')

time_theoretical = round(float(distance) / float(limit), 2)
time_actual = round(float(distance) / float(speed), 2)

time_saved = round(time_theoretical - time_actual, 2)

if time_saved > 0:
    print('Time saved: ' + str(time_saved) + 's')
else:
    print('Time gained: ' + str(abs(time_saved)) + 's')