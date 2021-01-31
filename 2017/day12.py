if __name__ == "__main__":
    f = open("day12.in", "r")
    data = [row.split(" <-> ") for row in f.read().splitlines()]
    f.close()

    data = [[row[0], [x.strip() for x in row[1].split(",")]] for row in data]

    connected = set()
    queue = ["0"]
    explored = set()
    while len(queue) > 0:
        curr = queue.pop()
        for row in data:
            if curr == row[0]:
                for nxt in row[1]:
                    connected.add(nxt)
                    if not nxt in explored:
                        queue.append(nxt)
            elif curr in row[1]:
                connected.add(row[0])
                if not row[0] in explored:
                    queue.append(row[0])
        explored.add(curr)

    print("Part A:", len(connected))

    toexplore = set([row[0] for row in data])
    groups = {}
    while len(toexplore) > 0:
        connected = set()
        explored = set()
        queue = [toexplore.pop()]
        first = queue[0]
        while len(queue) > 0:
            curr = queue.pop()
            for row in data:
                if curr == row[0]:
                    for nxt in row[1]:
                        connected.add(nxt)
                        if not nxt in explored:
                            queue.append(nxt)
                elif curr in row[1]:
                    connected.add(row[0])
                    if not row[0] in explored:
                        queue.append(row[0])
            explored.add(curr)
        for x in connected:
            if x in toexplore:
                toexplore.remove(x)
        groups[first] = connected

    print("Part B:", len(groups))
