class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = abs(
            min(self.__elements) - max(self.__elements))


# taking input
a = [int(num) for num in input().split(' ')]

difference = Difference(a)
difference.computeDifference()
print(difference.maximumDifference)
