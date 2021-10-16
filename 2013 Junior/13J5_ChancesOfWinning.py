teams = dict('1':0,'2':0,'3':0,'4':0)
favTeam = int(input())
numGamesPlayed = int(input())

for g in numGamesPlayed:
    game = [g for f in input().split()]

    if game[2] > game[3]:
        teams[game[0]] += 3
    elif game[3] > [2]:
        teams[game[1]] += 3
    else:
        teams[game[0]] += 1 
        teams[game[1]] += 1




