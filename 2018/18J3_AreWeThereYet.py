distances = [int(i) for i in input().split()]

cities = dict()

for i in range(len(distances)+1):
    city = i + 1
    for j in range(len(distances)+1):
        if i==j:
            dist = 0
        elif j > i:
            dist = sum(distances[i:j])
        else:
            dist = sum(distances[j:i])

        if city not in cities:
            cities[city] = [dist]
        else:
            cities[city].append(dist)

for value in cities.values():
    print(*value)
