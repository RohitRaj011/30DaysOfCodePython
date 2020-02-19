import math
import os


def diagonalDifference(arr):
    l = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0
    for i in range(l):
        for j in range(l):
            if i == j:
                primary_diagonal += arr[i][j]
            if i + j == l-1:
                secondary_diagonal += arr[i][j]
    return abs(primary_diagonal-secondary_diagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
