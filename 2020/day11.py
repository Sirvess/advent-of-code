from copy import deepcopy


def countAdjacent(y, x, currState, xMax, yMax):
    delta = (-1, 0, 1)
    count = 0
    for dy in delta:
        for dx in delta:
            y1 = y + dy
            x1 = x + dx
            if dy == dx == 0:
                continue
            if not ((x1 < 0) or (x1 > xMax) or (y1 < 0) or (y1 > yMax)):
                if currState[y1][x1] == "#":
                    count += 1
    return count


def countVisibleOccupied(y, x, currState, xMax, yMax):
    delta = (-1, 0, 1)
    count = 0
    for dy in delta:
        for dx in delta:
            y1 = y + dy
            x1 = x + dx
            if dy == dx == 0:
                continue
            while True:
                if (x1 < 0) or (x1 > xMax) or (y1 < 0) or (y1 > yMax):
                    break
                if currState[y1][x1] == "L":
                    break
                if currState[y1][x1] == "#":
                    count += 1
                    break
                y1 = y1 + dy
                x1 = x1 + dx

    return count


# mode = "adjacent" or "visible"
# adjacent used for pt A, visible for pt B
def findEquilibrium(data, mode):
    maxcount, countFunction = None, None
    if mode == "adjacent":
        maxcount = 3
        countFunction = countAdjacent
    elif mode == "visible":
        countFunction = countVisibleOccupied
        maxcount = 4
    else:
        print("Mode must be adjacent or visible")
        return -1

    currState = deepcopy(data)
    newstate = deepcopy(currState)
    while True:
        changed = False
        currState = deepcopy(newstate)
        newstate = deepcopy(currState)
        for y in range(0, len(data)):
            for x in range(0, len(data[0])):
                if currState[y][x] in ("L", "#"):
                    collisionCount = countFunction(
                        y, x, currState, len(data[0]) - 1, len(data) - 1
                    )
                    if currState[y][x] == "L":
                        if collisionCount == 0:
                            newstate[y][x] = "#"
                            changed = True
                    elif currState[y][x] == "#":
                        if collisionCount > maxcount:
                            newstate[y][x] = "L"
                            changed = True
        if changed == False:
            break

    return sum(
        [
            1
            for y in range(0, len(data))
            for x in range(0, len(data[0]))
            if currState[y][x] == "#"
        ]
    )


f = open("day11Input.txt", "r")
data = [[i for i in x] for x in f.read().splitlines()]
f.close()

print("Part A:", findEquilibrium(deepcopy(data), "adjacent"))
print("Part B:", findEquilibrium(deepcopy(data), "visible"))
