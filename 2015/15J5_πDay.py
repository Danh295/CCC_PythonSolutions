n = int(input())
k = int(input())

count = 0

def pie(pieces, people, m):
    global count

    if people == 1:
        count += 1
        return

    for i in range(m, pieces // people +1 ):
        pie(pieces-i, people-1, i)

pie(n, k, 1)
print(count)

