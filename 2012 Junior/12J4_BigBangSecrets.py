k = int(input())
word = list(input())

letters = [chr(i) for i in range(65, 91)]

for p in range(1,len(word)+1):
    char = word[p-1]
    i = letters.index(char)

    word[p-1] = letters[i-((3*p) + k)]


print(''.join(word))