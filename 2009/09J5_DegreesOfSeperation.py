relationships = {'6': ['2', '1','3','4','5','7'],
                '2': ['1'],
                '1': ['6'],
                '3': ['6','4','15'],
                '4': ['3','6','5'],
                '5':['6','4'],
                '7':['6','8'],
                '8': ['7','9'],
                '9': ['8','10','12'],
                '15': ['3','13'],
                '12': ['9','11'],
                '11': ['12','10'],
                '10': ['9','11'],
                '13':['15','14','12'],
                '14': ['13'],
                '16': ['18', '17'],
                '18': ['16','17'],
                '17': ['16','18']}

instruction = input()
x = input()
y = input()

def i(x, y):
    if x not in relationships:
        [x] = []
    elif y not in relationships:
        [y] = []
    else:
        if x not in [y]:
            relationships[y].append(x)
            relationships[x].append(y)
        else:
            pass
def d(x, y):
    [x].remove(y)
    [y].remove(x)
def n(x):
    return len(relationships[x])
def f(x):
    count = 0
    for person in [x]:
        count += len([person])

    return(count)
def s(x, y):
    queue = []
    visited = []
    count = 0

    queue.append(x)
    visited.append(x)

    while queue:
        currentNode = queue.pop(0)

        for i in relationships[currentNode]:
            
            if i not in visited:
                visited.append(currentNode)
                queue.append(i)
            else:
                print(currentNode)

if instruction == 'i':
    print(i(x,y))
elif instruction == 'd':
    print(d(x,y))
elif instruction == 'n':
    print(n(x))
elif instruction == 'f':
    print(f(x))
elif instruction == 's':
    print(s(x,y))
elif instruction == 'q':
    pass

        
