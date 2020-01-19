

# assume items is list
def insertionSort(items=[]):
    # split list into sorted and unsorted
    sortedIndex = 0

    while (sortedIndex + 1) < len(items):
        unsortedItem = items.pop(sortedIndex + 1)
        for insertionIndex in range(sortedIndex + 1):
            if items[insertionIndex] > unsortedItem:
                items.insert(insertionIndex, unsortedItem)
                break
            if insertionIndex == sortedIndex:
                items.insert(insertionIndex + 1, unsortedItem)
        sortedIndex += 1

    # for each element in unsorted...
        # insert the element into the correct place in sorted by:
        # store in temp var
        # shift all larger sorted elements to right by 1
        # insert the element after the first smaller


def insertionSort2(items=[]):
    sortedIndex = 1

    for sortedIndex in range(1, len(items)):
        unsortedElement = items[sortedIndex]
        i = sortedIndex
        while i > 0 and unsortedElement < items[i - 1]:
            items[i] = items[i - 1]
            i -= 1
        items[i] = unsortedElement


myList = [8, 6, 2, 3, 7, 9, 5, 0, 1, 4]

insertionSort2(myList)
print(myList)
