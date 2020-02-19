n = int(input())
count = 0
max_count = 0
binary = bin(n).replace("0b", "")
for i in binary:
    if i == '1':
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print(max_count)
