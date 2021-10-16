numRounds = int(input())

antoniaPts = 100
davidPts = 100

for r in range(numRounds):
    rnd = [a for a in input().split()]
    a = int(rnd[0])
    d = int(rnd[1])

    if a > d:
        davidPts -= a
    elif a < d:
        antoniaPts -= d
    else:
        continue

print(antoniaPts,davidPts, sep = '\n')

