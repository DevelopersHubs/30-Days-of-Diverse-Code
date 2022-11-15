#testscore3
lst = input().split(' ')
ab = [[], []]
for i in range(len(lst)):
    for k in range(0, int(lst[i])):
        ab[i].append(input())
for t in ab[1]:
    res = ''
    for p in range(len(ab[0])):
        if t not in ab[0]:
            res = -1
            break
        elif t == ab[0][p]:
            res = res + str(p + 1) + ' '
    print(res)