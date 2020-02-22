# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    return s


'''def check_magic(s):
    if np.sum(s, 0) == np.sum(s, 1):
        if np.trace(s) == np.sum(s, 0) and s[::-1].trace() == np.sum(s, 0):
            return 1
    else:
        return 0
'''

if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
