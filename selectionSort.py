
myList = [8, 6, 2, 3, 7, 9, 5, 0, 1, 4]


def selectionSort(items):
    # for each element in the array
        # compare it to each element to the right
        # track the lowest value
        # whichever was lowest, swap into current evaluator

    for i in range(len(items)):
        lowestIndex = i
        j = i
        while j < len(items):
            if items[j] < items[lowestIndex]:
                lowestIndex = j
            j += 1
        items[i], items[lowestIndex] = items[lowestIndex], items[i]


selectionSort(myList)
print(myList)
