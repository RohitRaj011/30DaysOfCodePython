def missingNumbers(arr, brr):
    unique = []
    for i in brr:
        if arr.count(i) != brr.count(i):
            unique.append(i)
        # remove instances of i from arr & brr
        arr = [x for x in arr if x != i]
        brr = [x for x in brr if x != i]
    unique.sort()
    return unique


n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))
result = missingNumbers(arr, brr)
for i in result:
    print(i, end=" ")
