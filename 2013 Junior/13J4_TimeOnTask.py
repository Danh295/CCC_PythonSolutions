numMinutes = int(input())
numChores = int(input())

choresMinutes = []
for chore in numChores:
    choresMinutes.append(input())

choresMinutes.sort()

while numMinutes > 0:

    for m in choresMinutes:
        numMinutes -= m

        if choresMinutes =