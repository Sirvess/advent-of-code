import hashlib

if __name__ == "__main__":
    f = open("day17.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    dooropen = ["b", "c", "d", "e", "f"]

    queue = [(data, (0, 0))]
    gridsize = 4
    gridr = range(4)

    done = False
    foundpaths = []
    while True:
        while len(queue) > 0:
            popped = queue.pop()
            currpath = popped[0]
            currpos = popped[1]
            if currpos[0] in gridr and currpos[1] in gridr:
                break
            if len(queue) == 0:
                done = True

        if done == True:
            break

        if currpos == (3, 3):
            path = currpath[len(data) :]
            foundpaths.append((path, len(path)))
            continue

        curr = hashlib.md5(currpath.encode("utf-8")).hexdigest()

        up = (curr[0], "U", (0, -1))
        down = (curr[1], "D", (0, 1))
        left = (curr[2], "L", (-1, 0))
        right = (curr[3], "R", (1, 0))

        for x in [up, down, left, right]:
            if x[0] in dooropen:
                queue.append(
                    (currpath + x[1], (currpos[0] + x[2][0], currpos[1] + x[2][1]))
                )

    foundpaths = sorted(foundpaths, key=lambda path: path[1])
    print("Part A:", foundpaths[0][0])
    print("Part B:", foundpaths[-1][1])
