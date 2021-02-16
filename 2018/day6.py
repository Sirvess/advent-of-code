from functools import reduce

if __name__ == "__main__":
    f = open("day6.in", "r")
    data = [[int(y) for y in x.split(", ")] for x in f.read().splitlines()]
    f.close()

    def getclosest(x, y, data):
        minrange = ("temp", 10000)  # a big number
        equalranges = 0
        for i, p in enumerate(data):
            currrange = abs(x - p[0]) + abs(y - p[1])
            if currrange == minrange[1]:
                equalranges += 1
            if currrange < minrange[1]:
                minrange = (str(i), currrange)
                equalranges = 0
        if equalranges > 0:
            return "."
        return minrange[0]

    coords = [
        ["." for i in range(500)] for i in range(500)
    ]  # arbitrary range larger than max coords

    for i, x in enumerate(data):
        coords[x[1]][x[0]] = str(i)

    for i, row in enumerate(coords):
        for j, val in enumerate(row):
            if not val == ".":
                continue
            closest = getclosest(j, i, data)
            coords[i][j] = closest

    toprow = set(coords[0])
    botrow = set(coords[-1])
    firstcol = set([x[0] for x in coords])
    lastcol = set([x[-1] for x in coords])
    infinites = reduce(
        lambda a, b: a.union(b), [toprow, botrow, firstcol, lastcol], set()
    )

    areamap = {str(x): 0 for x in range(len(data))}
    for x in coords:
        for val in x:
            if val in infinites:
                continue
            else:
                areamap[val] += 1
    print("Part A:", max([areamap[x] for x in areamap]))

    maxtotalrange = 10000
    fieldsize = 1000  # Choose sufficiently large
    origo = fieldsize // 2

    def oneifvalid(x, y, data):
        totaldistance = 0
        for i, p in enumerate(data):
            totaldistance += abs(x - p[0] - origo) + abs(y - p[1] - origo)
            if totaldistance >= maxtotalrange:
                return 0
        return 1

    areascovered = 0
    for i in range(fieldsize):
        for j in range(fieldsize):
            areascovered += oneifvalid(j, i, data)

    print("Part B:", areascovered)
