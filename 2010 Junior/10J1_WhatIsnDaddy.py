n = int(input())

visited = []
count = 0

for i in range(n):
    comb = [i, n-i]

    if sorted(comb) not in visited:
        count += 1
        visited.append(sorted(comb))
        print(comb)

    else:
        continue

print(count)