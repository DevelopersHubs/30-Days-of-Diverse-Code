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
#dealing with tuple and hash() function
if __name__ == '__main__':
    N = int(input())
    the_tuple = tuple([int(i) for i in input().split()])
    print(hash(the_tuple))
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
#swapcases
def swap_case(s):
    return (s.swapcase()) #Using the String method
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#testscore
def split_and_join(line):
    # write your code here
    return '-'.join(line.split())
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#testscore

# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello {} {}! You just delved into python.' .format(first,last))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
#testscore
def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    b= "".join(a)
    return b
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#testscore
def count_substring(string, sub_string):
    result = 0
    for i in range(0, len(string)):
        if string[i: len(sub_string) + i] == sub_string:
            result = result + 1
    return result
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#testscore
if __name__ == '__main__':
    s = input()
    ans =[0,0,0,0,0]
    for i in s:
        ans[0] = ans[0] or i.isalnum()
        ans[1] = ans[1] or i.isalpha()
        ans[2] = ans[2] or i.isdigit()
        ans[3] = ans[3] or i.islower()
        ans[4] = ans[4] or i.isupper()
    for i in range(len(ans)):
        print(ans[i])
