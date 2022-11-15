
#taking names and scores then print names with lowest scores

namesList = []
scoresList = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
        
    namesList.append(name)
    scoresList.append(score)
                
    secondLowestScore = sorted(list(set(scoresList)), reverse=False)[1]
    
    namesSecondLowestScore = [name for idx, name in enumerate(namesList) if(scoresList[idx]==secondLowestScore) ]
    