# Done

text = ('ABCCDEABAA')
string = list('ABCDE')
    
def cyclicShift(text, string):
    string = list(string)

    for i in string:
        cyclic_shift = []

        temp = string[0]
        string = string[1:]

        string.append(temp)
        cyclic_shift.extend(string)

        print(cyclic_shift)
        cyclic_shift = "".join(cyclic_shift)

        if cyclic_shift in text:
            return 'yes'

        else:
            continue

    return

print(cyclicShift('ABCCDEABAA','ABCDE'))




    