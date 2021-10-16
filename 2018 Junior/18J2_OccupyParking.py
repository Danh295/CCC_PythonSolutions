n = int(input())

d1 = list(input())
d2 = list(input())

count = 0
for o, t in zip(d1, d2):
    if o == t and o == 'C':
        count += 1

print(count)