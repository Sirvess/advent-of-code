from numpy import loadtxt
import functools

# Returns list of entries that fit criteria
# targetSum is the sum that the sum of numElements of input should equal
# Returns list of those elements


def findMatchingEntries(targetSum, numElements, inData):
    for x in inData:
        if(numElements == 2):
            if (targetSum - x) in inData:
                return [x, targetSum-x]
        else:
            nextIteration = findMatchingEntries(
                targetSum-x, numElements-1, filter(lambda a: targetSum - x - a >= 0, inData))
            if(nextIteration != False):
                return [*nextIteration, x]
    return False


def printResults(results):
    if(results):
        print("Matching entries: ", results)
        print("Entries multiplied: ", functools.reduce(lambda a, b: a*b, results))
    else:
        print("Found no matching entries.")


if __name__ == "__main__":
    f = open("day1Input.txt", "r")
    inData = loadtxt(f, int)
    f.close()

    partA = findMatchingEntries(2020, 2, inData)
    printResults(partA)

    partB = findMatchingEntries(2020, 3, inData)
    printResults(partB)
