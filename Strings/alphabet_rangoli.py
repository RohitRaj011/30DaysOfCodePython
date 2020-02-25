def print_rangoli(size):
    for row in range(size, 0, -1):
        for _ in range(2 * row - 2):
            print('-', end='')
        for j in range(size, row-1, -1):
            if row == size:
                print(chr(96+j), end='')
            else:
                print(chr(96+j) + '-', end='')
        for k in range(j+1, size+1):
            print(chr(96+k), end='')
            if k != size:
                print('-', end='')
        for _ in range(-1, 2 * row - 3):
            print('-', end='')
        print('\r')

    for row in range(1, size):
        for _ in range(2 * row):
            print('-', end='')
        for j in range(size, row, -1):
            print(chr(96+j) + '-', end='')
        for k in range(j+1, size+1):
            print(chr(96+k) + '-', end='')
        for _ in range(2 * row - 1):
            print('-', end='')
        print('\r')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
