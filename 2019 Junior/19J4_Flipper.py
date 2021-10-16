grid = [1, 2,
        3, 4]

ins = list(input())

for i in ins:

    if i == 'H':

        for j in range(len(grid)):
            n = grid[j]

            if n - 2 <= 0:
                grid[j] += 2
            else:
                grid[j] -= 2

    elif i == 'V':

        for j in range(len(grid)):
            if j == 0 or j == 2:
                temp = grid[j+1]
            
            grid.insert(j, temp)
            temp = grid.pop(j+1)

print(*grid[0:2])
print(*grid[2:4])

        
            


