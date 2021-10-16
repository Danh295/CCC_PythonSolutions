num = []
t = False

for _ in range(4):
    num.append(input())

if num[0] == '8' or num[0] == '9':
    if num[1] == num[2] and (num[3] == '8' or num[3] == '9'):
        t = True
    else:
        pass

if t == True:
    print('ignore')
else:
    print('answer')
    

