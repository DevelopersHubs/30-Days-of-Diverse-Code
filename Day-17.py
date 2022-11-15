
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
