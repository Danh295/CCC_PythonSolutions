num = int(input())
shift = int(input())

shiftySum = 0
for i in range(shift):
    num += num*10*i
    shiftySum 