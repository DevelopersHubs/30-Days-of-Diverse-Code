#dealing with tuple and hash() function
if __name__ == '__main__':
    N = int(input())
    the_tuple = tuple([int(i) for i in input().split()])
    print(hash(the_tuple))