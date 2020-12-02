import functools

# Returns list of entries that fit criteria
# targetSum is the sum that the sum of numElements of input should equal
# Returns list of those elements


def findMatchingEntries(targetSum, numElements, inData):
    for x in inData:
        if numElements == 2:
            if (targetSum - x) in inData:
                return [x, targetSum - x]
        else:
            nextIteration = findMatchingEntries(
                targetSum - x,
                numElements - 1,
                list(filter(lambda a: targetSum - x - a >= 0, inData)),
            )
            if nextIteration != False:
                return [*nextIteration, x]
    return False


def printResults(results):
    if results:
        print("Matching entries: ", results)
        print("Entries multiplied: ", functools.reduce(lambda a, b: a * b, results))
    else:
        print("Found no matching entries.")


def formatInData(data):
    return list(map(lambda x: int(x[:-1]), data))


if __name__ == "__main__":
    f = open("day1Input.txt", "r")
    inData = f.readlines()
    f.close()

    formattedData = formatInData(inData)

    partA = findMatchingEntries(2020, 2, formattedData)
    printResults(partA)

    partB = findMatchingEntries(2020, 3, formattedData)
    printResults(partB)
