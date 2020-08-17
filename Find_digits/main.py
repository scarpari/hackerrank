import os

def findDigits(n):
    count = 0
    string = str(n)
    for i in string:
        m = int(i)
        if m!=0 and n%m == 0:
            count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
