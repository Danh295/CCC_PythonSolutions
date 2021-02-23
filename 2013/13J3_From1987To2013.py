# year = int(input())

# while True:
#     year += 1
    
#     yrLst = list(str(year))
#     distinct = []

#     for y in yrLst:
#         if y not in distinct:
#             distinct.append(y)
#         else:
#             continue

#     if len(distinct) == len(yrLst):
#         print(year)
#         break

#     else:
#         continue

start_year = int(input())
increment = 1

while(True):
    next_year = start_year + increment
    visited = []
    unique_flag = 0

    while(next_year>0):
        digit = next_year%10

        if digit in visited:
            unique_flag+=1
            break

        visited.append(digit)
        next_year = next_year//10

    if unique_flag==0:
        next_year = start_year + increment
        break

    increment+=1



print(next_year)