#Done
speed_limit = int(input())
recorded_speed = int(input())

if recorded_speed <= speed_limit:
    print('Congratulations, you are within the speed limit!')

else:
    speed_over_limit = recorded_speed - speed_limit

    if speed_over_limit <= 20:
        fine = 100
    elif speed_over_limit <= 30:
        fine = 270
    else:
        fine = 500

    print('You are speeding and your fine is $'+str(fine)+'.')
