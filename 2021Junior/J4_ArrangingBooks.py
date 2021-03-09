shelf = list(input())

numL = shelf.count('L')
numM = shelf.count('M')
numS = shelf.count('S')

secL = shelf[0:numL]
secM = shelf[numL:numL+numM]
secS = shelf[numL+numM:]

swapsL = secL.count('M')
swapsM = secM.count('L')

swapsLM = max(swapsL, swapsM)

swapsS = secS.count('M')+secS.count('L')

totalSwaps = swapsLM + swapsS

print(totalSwaps)

#question for algo: can't by swapping the different element change
#the number of swaps required to do smt? Why?