from itertools import combinations_with_replacement as cwr

word, count = input().split()

output = map("".join,cwr(sorted(word),int(count)))
print(*output,sep="\n")