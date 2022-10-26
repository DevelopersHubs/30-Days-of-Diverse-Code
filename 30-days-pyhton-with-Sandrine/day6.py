# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for test_case in range(n):
    s = input()
    even_char = ''
    odd_char = ''

    for i in range(len(s)):
        if i%2 == 0:
            even_char += s[i]
        else:
            odd_char += s[i]
    
    print(f'{even_char} {odd_char}')