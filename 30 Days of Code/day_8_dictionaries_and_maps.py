from sys import stdin

n = int(input())  # number of inputs
phone_book = {}  # define dictionary

# taking values and putting it into dictionary
for i in range(n):
    entry = input().split()
    phone_book[entry[0]] = entry[1]

# taking queries
query = stdin.read().splitlines()

# searching the queries and printing output
for i in range(len(query)):
    if query[i] in phone_book:
        print(query[i] + "=" + phone_book[query[i]])
    else:
        print("Not found")
