from copy import deepcopy

if __name__ == "__main__":
    f = open("day22.in", "r")
    data = f.read().splitlines()
    f.close()

    padding = 1000
    initmap = [["." for i in range(padding)] for x in range(padding)]
    origin = (padding - len(data)) // 2
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            initmap[origin + i][origin + j] = data[i][j]

    startpos = (origin + len(data) // 2, origin + len(data) // 2)
    startbearing = "N"
    statemap = deepcopy(initmap)

    nextbearing = {
        "left": {"N": "W", "E": "N", "S": "E", "W": "S"},
        "right": {"N": "E", "E": "S", "S": "W", "W": "N"},
    }

    burstcount = 0
    infectioncount = 0
    pos = startpos
    bearing = startbearing
    while burstcount < 10000:
        if statemap[pos[1]][pos[0]] == ".":
            statemap[pos[1]][pos[0]] = "#"
            infectioncount += 1
            bearing = nextbearing["left"][bearing]

        elif statemap[pos[1]][pos[0]] == "#":
            statemap[pos[1]][pos[0]] = "."
            bearing = nextbearing["right"][bearing]

        if bearing == "N":
            pos = (pos[0], pos[1] - 1)
        elif bearing == "W":
            pos = (pos[0] - 1, pos[1])
        elif bearing == "S":
            pos = (pos[0], pos[1] + 1)
        elif bearing == "E":
            pos = (pos[0] + 1, pos[1])
        burstcount += 1

    print("Part A:", infectioncount)

    statemap = deepcopy(initmap)
    burstcount = 0
    infectioncount = 0
    pos = startpos
    bearing = "N"
    while burstcount < 10000000:
        if statemap[pos[1]][pos[0]] == ".":
            statemap[pos[1]][pos[0]] = "W"
            bearing = nextbearing["left"][bearing]
        elif statemap[pos[1]][pos[0]] == "#":
            statemap[pos[1]][pos[0]] = "F"
            bearing = nextbearing["right"][bearing]
        elif statemap[pos[1]][pos[0]] == "W":
            infectioncount += 1
            statemap[pos[1]][pos[0]] = "#"
        elif statemap[pos[1]][pos[0]] == "F":
            statemap[pos[1]][pos[0]] = "."
            # Reversing by turning right twice
            bearing = nextbearing["right"][bearing]
            bearing = nextbearing["right"][bearing]

        if bearing == "N":
            pos = (pos[0], pos[1] - 1)
        elif bearing == "W":
            pos = (pos[0] - 1, pos[1])
        elif bearing == "S":
            pos = (pos[0], pos[1] + 1)
        elif bearing == "E":
            pos = (pos[0] + 1, pos[1])
        burstcount += 1

    print("Part B:", infectioncount)
