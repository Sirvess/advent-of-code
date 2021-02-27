from copy import deepcopy


def getadj(i, j, prevfield):
    x = [-1, 0, 1]
    y = [-1, 0, 1]
    adjs = []
    for dx in x:
        for dy in y:
            ynew = i + dy
            xnew = j + dx
            if not (
                dy == dx == 0
                or (
                    ynew > len(prevfield) - 1
                    or xnew > len(prevfield) - 1
                    or ynew < 0
                    or xnew < 0
                )
            ):
                adjs.append(prevfield[ynew][xnew])
    return adjs


def fieldgen(initialstate):
    prevfield = deepcopy(initialstate)
    while True:
        currfield = deepcopy(prevfield)
        for i, row in enumerate(prevfield):
            for j, val in enumerate(row):
                adj = getadj(i, j, prevfield)
                if val == ".":
                    currfield[i][j] = "|" if adj.count("|") >= 3 else "."
                if val == "|":
                    currfield[i][j] = "#" if adj.count("#") >= 3 else "|"
                if val == "#":
                    currfield[i][j] = (
                        "#" if adj.count("#") >= 1 and adj.count("|") >= 1 else "."
                    )
        prevfield = deepcopy(currfield)

        trees = sum([row.count("|") for row in prevfield])
        yards = sum([row.count("#") for row in prevfield])
        yield trees * yards


if __name__ == "__main__":
    f = open("day18.in", "r")
    data = [list(x) for x in f.read().splitlines()]
    f.close()

    fieldgenerator = fieldgen(data)
    for i in range(10):
        score = next(fieldgenerator)
    print("Part A:", score)

    fieldgenerator = fieldgen(data)
    loop = []
    loopstart = 0
    looplength = 0
    foundnumbers = set()
    loopset = set()
    iterations = 0
    while True:
        score = next(fieldgenerator)
        if score in foundnumbers:
            if loopstart == 0:
                loopstart = iterations
            if score in loopset and len(loop) == 28:
                # HACK: Somewhat naive, entire round throuh loop.
                # Found actual looplength through manual testing
                break
            looplength += 1
            loopset.add(score)
            loop.append(score)
        else:
            loopstart = 0
            looplength = 0
            loop = []
            loopset = set()
        foundnumbers.add(score)
        iterations += 1
    print("Part B:", loop[((1000000000 - loopstart - 1) % looplength)])
