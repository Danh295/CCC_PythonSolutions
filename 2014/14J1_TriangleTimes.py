lengths = []
for i in range(3):
    lengths.append(int(input()))

if sum(lengths) != 180:
    print('Error')

elif lengths[0] == lengths[1] == lengths[2]:
    print('Equilateral')

elif lengths[0] != lengths[1] != lengths[2]:
    print('Scalene')

else:
    print('Isosceles')