#let her travel speed be 60km/h
#meaning her total distance to travel is 120km

dTime = [int(i) for i in input().split(':')]
depart = dTime[0]*60 + dTime[1]

rush1s = 7*60
rush1e = 10*60
rush2s = 15*60
rush2s = 19*60

t = 240
while t > 0:
    if depart > rush1s and depart < rush1e:
        t -= 1
    elif depart > rush2s and depart < rush2e:
        t -= 1
    else:
        t -= 2

    depart += 1

hour = depart//60 
depart -= hour*60

print(str(hour)+':'+str(depart))
