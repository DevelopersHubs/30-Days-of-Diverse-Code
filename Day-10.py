#collection.counter()
from collections import Counter
X=int(input())
Y=Counter(map(int,input().split()))
N=int(input())     # Number of customers
total=0
for i in range (N):
    size,price=map(int,input().split())
    if Y[size]:
        total+=price
        Y[size]-=1
print(total)