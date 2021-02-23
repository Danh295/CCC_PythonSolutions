apples = []
bananas = []

for a in range(3):
    apples.append(int(input()))

for b in range(3):
    bananas.append(int(input()))

apples[0] *= 3
apples[1] *= 2

bananas[0] *= 3
bananas[1] *= 2

if sum(apples) > sum(bananas):
    print('A')
elif sum(bananas) > sum(apples):
    print('B')
else:
    print('T')

