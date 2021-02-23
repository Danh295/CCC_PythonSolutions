word = input()

def palindrome():
    n = len(word)
    # print(n)

    maxLen = 0

    if n == 1:
        return(1)
    
    for i in range(n):
        for j in range(i+1, n):

            sub = word[i:j+1]
            # print('substring: ',sub)

            if len(sub) % 2 == 0:
                x = len(sub) // 2
                # print(sub[:x], sub[x:][::-1])

                if sub[:x] == sub[x:][::-1]:
                    if len(sub) > maxLen:
                        maxLen = len(sub)
            else:
                x = (len(sub) // 2) + 1
                # print(sub[:x], sub[x-1:][::-1])

                if sub[:x] == sub[x-1:][::-1]:
                    if len(sub) > maxLen:
                        maxLen = len(sub)

    return(maxLen)

print(palindrome())
