
#testcase1
#dealing with the map function
n = int(input())
arr = map(int, input().split())
arr_unique = list(set(arr))
arr_unique.sort()
print(arr_unique[-2])