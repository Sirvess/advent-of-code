def countviablepairs(data):

    pairscount = 0

    for i in range(len(data)):
        nodeA = data[i]
        nodeAavail = nodeA[-2]
        nodeAused = nodeA[-3]

        nodeAcoords = (
            int(nodeA[0].split("-")[1][1:]),
            int(nodeA[0].split("-")[2][1:]),
        )

        for j in range(i + 1, len(data)):
            nodeB = data[j]
            nodeBavail = nodeB[-2]
            nodeBused = nodeB[-3]

            nodeBcoords = (
                int(nodeB[0].split("-")[1][1:]),
                int(nodeB[0].split("-")[2][1:]),
            )

            # A,B
            if not nodeAused == "0T":
                if not nodeAcoords == nodeBcoords:
                    if int(nodeAused[:-1]) <= int(nodeBavail[:-1]):
                        pairscount += 1

            # B,A
            if not nodeBused == "0T":
                if not nodeAcoords == nodeBcoords:
                    if int(nodeBused[:-1]) <= int(nodeAavail[:-1]):
                        pairscount += 1
    return pairscount


if __name__ == "__main__":
    f = open("day22.in", "r")
    data = [row.split() for row in f.read().splitlines()]
    f.close()

    # Filesystem', 'Size', 'Used', 'Avail', 'Use%'
    # First 2 indeces not relevant
    print("Part A:", countviablepairs(data[2:]))
