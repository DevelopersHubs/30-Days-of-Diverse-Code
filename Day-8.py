#lists
#testcore0
#insert,delete,sort and reverse array
N = int(input())
list_=[]    
query=[]

for i in range(N):
    x=input().split()
    query.append(x)

for i in query:    
    #print(i[0])
    if i[0]=='append':
        list_.append(int(i[1]))
    elif i[0]=='insert':
        list_.insert(int(i[1]),int(i[2]))
    elif i[0]=='print':
        print(list_)
    elif i[0]=='remove':
        list_.remove(int(i[1]))
    elif i[0]=='sort':
        list_.sort()
    elif i[0]=='pop':
        list_.pop()
    elif i[0]=='reverse':
        list_.reverse()