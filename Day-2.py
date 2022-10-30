#list comprehension
#testcase0
x = int(input())
y = int(input())
z = int(input())
n = int(input())
res=[[i,j,k] for i in range(x+1)for j in range(y+1)for k in range(z+1) if i+j+k!=n]
print(res)
#testcase1
#dealing with the map function
n = int(input())
arr = map(int, input().split())
arr_unique = list(set(arr))
arr_unique.sort()
print(arr_unique[-2])
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
    
    print('\n'.join(sorted(namesSecondLowestScore)))
#testcase2
#key value and division of marks to 2dp
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input()
print("{0:.2f}".format(sum(student_marks[query_name])/3))  