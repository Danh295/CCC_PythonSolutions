depths = []
for _ in range(4):
    depth = int(input())
    depths.append(depth)

if depths[0] < depths[1] and depths[1] < depths[2] and depths[2] < depths[3]:
    print('Fish Rising')
elif depths[0] > depths[1] and depths[1] > depths[2] and depths[2] > depths[3]:
    print('Fish Diving')
elif depths[0] == depths[1] and depths[1] == depths[2] and depths[2] == depths[3]:
    print('Constant Depth')
else:
    print('No Fish')

# rising = []
# diving = []
# constant = []
# for d in range(len(depths)-1):
#     if depths[d] < depths[d+1]:
#         rising.append('T')

#     elif depths[d] > depths[d+1]:
#         diving.append('T')
    
#     elif depths[d] == depths[d+1]:
#         constant.append('T')

# if len(rising) == 3:
#     print('Fish Rising')
# elif len(diving) == 3:
#     print('Fish Diving')
# elif len(constant) == 3:
#     print('Constant Depth')
# else:
#     print('No Fish')       
    
#first case wasnt successful on Demoj
