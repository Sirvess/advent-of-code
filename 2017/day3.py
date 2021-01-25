if __name__ == "__main__":
    f = open("day3.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    pos = [0, 0]
    explored = set()
    explored.add(tuple(pos))
    direction = "r"
    for i in range(0, data - 1):
        # right, up, left, down, right,
        if direction == "r":
            pos[0] += 1
            comparepos = tuple([pos[0], pos[1] + 1])
        elif direction == "l":
            pos[0] -= 1
            comparepos = tuple([pos[0], pos[1] - 1])
        elif direction == "d":
            pos[1] -= 1
            comparepos = tuple([pos[0] + 1, pos[1]])
        elif direction == "u":
            pos[1] += 1
            comparepos = tuple([pos[0] - 1, pos[1]])

        if comparepos not in explored:
            if direction == "r":
                direction = "u"
            elif direction == "l":
                direction = "d"
            elif direction == "d":
                direction = "r"
            elif direction == "u":
                direction = "l"

        explored.add(tuple(pos))
    print("Part A:", sum([abs(x) for x in pos]))

    def getneighbors(position, explored):
        ranges = [-1, 0, 1]
        neighbs = []
        for i in ranges:
            for j in ranges:
                if i == j == 0:
                    continue
                if tuple([position[0] + i, position[1] + j]) in explored:
                    neighbs.append(tuple([position[0] + i, position[1] + j]))
        return neighbs

    pos = [0, 0]
    explored = set()
    explored.add(tuple(pos))
    direction = "r"
    exploredvals = {}
    lastsum = 1
    exploredvals[tuple([0, 0])] = lastsum
    while lastsum < data:
        if direction == "r":
            pos[0] += 1
            comparepos = tuple([pos[0], pos[1] + 1])
        elif direction == "l":
            pos[0] -= 1
            comparepos = tuple([pos[0], pos[1] - 1])
        elif direction == "d":
            pos[1] -= 1
            comparepos = tuple([pos[0] + 1, pos[1]])
        elif direction == "u":
            pos[1] += 1
            comparepos = tuple([pos[0] - 1, pos[1]])

        if comparepos not in explored:
            if direction == "r":
                direction = "u"
            elif direction == "l":
                direction = "d"
            elif direction == "d":
                direction = "r"
            elif direction == "u":
                direction = "l"

        neighbs = getneighbors(pos, explored)
        lastsum = sum([exploredvals[n] for n in neighbs])
        exploredvals[tuple(pos)] = lastsum
        explored.add(tuple(pos))

    print("Part B:", lastsum)
