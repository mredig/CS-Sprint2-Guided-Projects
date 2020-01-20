import random

myList = [8, 6, 2, 3, 7, 9, 5, 0, 1, 4]


def bubbleSort(items):
    # iterate over the array
    # compare each element to neighbor, swap if the item on right is lower
    # track if there were any swaps or not
    # if there aren't, sorting done

    swapped = True
    while swapped:
        swapped = False
        print(items)
        for index, value in enumerate(items):
            if index == 0:
                continue
            if value < items[index - 1]:
                items[index - 1], items[index] = items[index], items[index - 1]
                swapped = True
    return items


random.shuffle(myList)
bubbleSort(myList)
print(myList)
