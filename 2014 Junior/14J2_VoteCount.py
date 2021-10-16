numVotes = int(input())
votes = list(input())

countA = 0
countB = 0

for vote in votes:
    if vote == 'A':
        countA += 1
    elif vote == 'B':
        countB += 1

if countA > countB:
    print('A')
elif countA < countB:
    print('B')
else:
    print('Tie')


