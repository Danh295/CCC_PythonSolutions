trout = int(input())
pike = int(input())
pickerel = int(input())
totalPts = int(input())

maxTrout = totalPts // trout
maxPike = totalPts // pike
maxPickerel = totalPts // pickerel

countTrout = 0
countPike = 0
countPickerel = 0
count = 0

for i in range(maxTrout+1):

    for j in range(maxPike+1):        

        for k in range(maxPickerel+1):

            if i == j and j == k:
                continue

            else:
                if (i*trout) + (j*pike) + (k*pickerel) <= totalPts:
                    print(i,'Brown Trout',j,'Northern pIke',k,'Yellow Pickerel')

                    count += 1

print('Number of ways to catch fish: ', count)