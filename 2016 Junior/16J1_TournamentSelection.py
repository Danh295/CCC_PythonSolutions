games = []
for _ in range(6):
    games.append(input())

if games.count('W') == 0:
    print(-1)
elif games.count('W') < 3:
    print(3)
elif games.count('W') < 5:
    print(2)
else:
    print(1)
    