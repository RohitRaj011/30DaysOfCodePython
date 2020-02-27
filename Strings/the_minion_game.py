def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if vowel(string[i]):
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


def vowel(x):
    return x in 'AEIOU'


if __name__ == '__main__':
    s = input()
    minion_game(s)
