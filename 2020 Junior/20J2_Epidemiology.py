p = int(input())
n = int(input())
r = int(input())

days = 0

l = n
while l <= p:
    days += 1
    n = n*r
    l += n

print(days)
