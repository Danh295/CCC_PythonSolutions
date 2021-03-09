n = []

ins = []
while n != ['9', '9', '9', '9', '9']:
    n = list(input())
    ins.append(n)
ins.remove(n)

d = ''
for i in ins:
    steps = 0
    dig1 = int(i[0])
    dig2 = int(i[1])
    s = dig1 + dig2

    if s % 2 != 0:
        d = 'left'
    elif s % 2 == 0 and s != 0:
        d = 'right'
    else:
        pass

    steps = int(''.join(i[2:]))

    print(d, steps)
        