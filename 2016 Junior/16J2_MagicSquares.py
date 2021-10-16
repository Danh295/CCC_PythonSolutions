row = dict()

for i in range(4):
    row[i] = []
    temp = [int(i) for i in input().split()]
    row[i].append(temp)

column = dict()
for i in range(4):
    column[i] = []
    print([row[0][i], row[1][i], row[2][i], row[3][i]])
    column[i].append(temp)

rsum = sum(row[1])
csum = sum(column[1])

for i in range(4):
    if sum(row[i]) == s:
        if sum(column[i]) == s:
            print('magic')
        else:
            break
    else:
        print('not magic')

