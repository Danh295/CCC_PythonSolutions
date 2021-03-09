n = int(input())
names = []
bids = []
for i in range(n):
    names.append(input())
    bids.append(int(input()))

maxBid = max(bids)
for i, j in zip(names, bids):
    if j == maxBid:
        print(i)
        break



