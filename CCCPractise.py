# grid = {'box1':[1,2], 'box2':[2,2],'box3':[1,1],'box4':[2,1]}

# inp = [char for char in input().split()]

# for action in inp:

#     if action == 'H':

#         for box in grid:
#             temp = box[0]
#             grid.replace(box[0],box[1])
#             grid.replace(box[1],temp)

#     if action == 'V':

#         for box in grid:
#             tmep = box[1]
#             grid.replace(box[1],box[0])
#             grid.replace(box[0],temp)

# print(grid)

moves = input()

arr = [1,2,
        3,4]

for move in moves:

    if move == 'H':
        arr[0], arr[2] = arr[2], arr[0]
        arr[1], arr[3] = arr[3], arr[1]

    if move == 'V':
        arr[0], arr[1] = arr[1], arr[0]
        arr[2], arr[3] = arr[3], arr[2]

print(arr[0],arr[1])
print(arr[2],arr[3])