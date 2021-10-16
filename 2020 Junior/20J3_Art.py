numDrops = int(input())

drops = []
for i in range(numDrops):
    temp = [int(i) for i in input().split(',')]
    drops.append(temp)

minx = 100
miny = 100
maxx = 0
maxy = 0

for x, y in drops:
    if x < minx:
        minx = x
    elif x > maxx:
        maxx = x
    
    if y < miny:
        miny = y
    elif y > maxy:
        maxy = y

print(str(minx-1)+','+str(miny-1)+'\n'+str(maxx+1)+','+str(maxy+1))
