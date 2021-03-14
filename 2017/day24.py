def getbridgecands(data):
    bfs = []  # list of (paths, last)
    paths = []

    # Get initials for bfs
    for x in data:
        a, b = map(int, x.split("/"))
        if 0 == a:
            bfs.append(([x], b))
        elif 0 == b:
            bfs.append(([x], a))

    while len(bfs) > 0:
        prevqueue = bfs.pop()
        prevbridge = prevqueue[1]

        added = False
        for x in data:
            if x in prevqueue[0]:
                continue
            a, b = map(int, x.split("/"))
            if prevbridge == a:
                added = True
                bfs.append(([*prevqueue[0], x], b))
            elif prevbridge == b:
                added = True
                bfs.append(([*prevqueue[0], x], a))
        if not added:
            paths.append(prevqueue[0])

    return paths


def getbridgestrength(bridges):
    return sum([sum(map(int, b.split("/"))) for b in bridges])


if __name__ == "__main__":
    f = open("day24.in", "r")
    data = f.read().splitlines()
    f.close()

    strengths = set()
    bridgecands = getbridgecands(data)
    for cand in bridgecands:
        strengths.add(getbridgestrength(cand))

    print("Part A:", max(strengths))

    lengths = {}
    bridgecands = getbridgecands(data)
    for cand in bridgecands:
        if len(cand) in lengths:
            lengths[len(cand)] = max(getbridgestrength(cand), lengths[len(cand)])
        else:
            lengths[len(cand)] = getbridgestrength(cand)

    print("Part B:", lengths[max(lengths)])
