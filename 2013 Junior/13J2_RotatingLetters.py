letters = ['I','O','S','H','Z','X','N']

word = list(input())

answer = 'YES'
for char in word:
    if char not in letters:
        answer = 'NO'

print(answer)
