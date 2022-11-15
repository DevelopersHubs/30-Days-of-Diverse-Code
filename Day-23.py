
# Complete the solve function below.
import string
def solve(s):
    if 0 < len(s) < 1000:
       return string.capwords(s,' ')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
