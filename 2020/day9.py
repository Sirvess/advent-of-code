def isSumOfTwo(num, cands):
    for item in cands:
        if (num - item) in cands:
            return True
    return False


def findFirstInvalid(data, windowLength):
    for i in range(windowLength + 1, len(data) - 1):
        if not isSumOfTwo(data[i], data[i - windowLength : i]):
            return data[i]
    print("No invalid found")


def partB(num):
    l = 0
    r = 1

    while l < len(data) - 1 and r < len(data):
        currsum = sum(data[l:r])
        if currsum == num:
            return max(data[l:r]) + min(data[l:r])
            break
        elif currsum > num:
            l += 1
            if l == r:
                r += 1
        else:
            r += 1
    print("Not found")


if __name__ == "__main__":
    f = open("day9Input.txt", "r")
    data = [int(x) for x in f.read().splitlines()]
    f.close()

    # Part A

    firstInvalidNumber = findFirstInvalid(data, 25)
    print("Part A:", firstInvalidNumber)

    # Part B

    print("Part B:", partB(firstInvalidNumber))
