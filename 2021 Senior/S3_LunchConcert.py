N = int(input())

friends = []

for _ in range(N):
    friends.append(list(map(int, input().split())))

def distance(pos):
    dist = 0
    for p,w,d in friends:
        if pos > p:
            if pos <= p + d:
                continue
            dist += (pos - (p + d)) * w
        else:
            if pos >= p - d:
                continue
            dist += ((p - d) - pos) * w

    return dist

left = 0
right = 1000000001

while left < right:
    mid = (left + right) // 2
    if distance(mid) < distance(mid + 1):
        right = mid
    else:
        left = mid + 1

print(distance(left))