import string
def print_rangoli(size):
    # your code goes here
    nor=''
    rev=''
    down=[]
    for i in range(size-1,-1,-1): #upper
        strr=string.ascii_letters[i]
        strr1= rev+strr+nor
        nor=string.ascii_letters[i]+nor
        rev=rev+string.ascii_letters[i]
        strr1= '-'.join(strr1)
        strr1= '-'*i*2 + strr1 +'-'*i*2
        print(strr1)
        down.append(strr1)
    for i in range(size-2,-1,-1):
        print(down[i])
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)