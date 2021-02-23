numLines = int(input())

message = dict()
for i in range(numLines):
    message[i] = input().split()

for n in message.keys():
    print(int(message[n][0])*message[n][1])