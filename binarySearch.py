

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")


def binarySearch(toFind, items=[], count=1):
    if len(items) == 0:
        return False
    midpoint = len(items) // 2
    mid = items[midpoint]

    # print(toFind, items, mid)

    if toFind == mid:
        return (True, count)
    elif toFind < mid:
        return binarySearch(toFind, items[:midpoint], count + 1)
    else:
        return binarySearch(toFind, items[midpoint + 1:], count + 1)


# print(binarySearch("p", alpha))

# print(binarySearch("V", alpha))

numbers = list(range(2**9))

for number in numbers:
    _, count = binarySearch(number, numbers)
    print(number, count)
