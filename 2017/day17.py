if __name__ == "__main__":
    f = open("day17.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    iterations = 2017
    steps = data

    arr = [0]
    i = 1
    pos = 0
    for j in range(iterations):
        nextindex = pos + steps
        if nextindex >= i:
            nextindex = (nextindex - i) % i
        nextindex += 1

        arr.insert(nextindex, i)
        i += 1
        pos = nextindex
    print("Part A:", arr[pos + 1])

    iterations = 50000000

    arr = [0]
    i = 1
    pos = 0
    rest = 0
    for j in range(iterations):
        nextindex = pos + steps
        if nextindex >= i:
            nextindex = (nextindex - i) % i
        nextindex += 1

        if nextindex == 1:
            rest = i
        pos = nextindex
        i += 1
    print("Part B:", rest)
