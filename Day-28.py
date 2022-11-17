from itertools import combinations

s,k=input().split()

s=sorted(str(s).upper())
k=int(k)

for i in range(k):
    comb=(combinations(s,i+1))
    print(*sorted(map(''.join, comb)), sep="\n")