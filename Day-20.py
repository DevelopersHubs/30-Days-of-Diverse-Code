n, m = [int(x) for x in input().split()]
ptrn = ".|."
for i in range(1,n,2):
    print((ptrn*i).center(m, "-"))
    
print("WELCOME".center(m, "-"))

for i in range(n-2,0,-2):
    print((ptrn*i).center(m, "-"))