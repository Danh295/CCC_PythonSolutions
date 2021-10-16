question = int(input())
numCitizens = int(input())

dmojSpeeds = [int(s) for s in input().split()]
pegSpeeds = [int(s) for s in input().split()]


total_speed = 0
for i in range(numCitizens):

    if question == 1:
        dmojSpeeds.sort(reverse=True)
        pegSpeeds.sort(reverse=True)
        speed1 = dmojSpeeds[i]
        speed2 = pegSpeeds[i]
        total_speed += max(speed1, speed2)

    else:
        dmojSpeeds.sort(reverse=True)
        pegSpeeds.sort()
        speed1 = dmojSpeeds[i]
        speed2 = pegSpeeds[i]
        total_speed += max(speed1, speed2)

print(total_speed)