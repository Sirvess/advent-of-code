if __name__ == "__main__":
    f = open("day7.in", "r")
    data = f.read().splitlines()
    f.close()

    accs = set()
    weights = {}
    children = {}
    for row in data:
        cand = row.split(" ")
        weights[cand[0]] = int(cand[1][1:-1])
        accs.add(cand[0])
        if "->" in row:
            cands = row.split(" -> ")[1].split(", ")
            children[cand[0]] = cands

    for row in data:
        if "->" in row:
            cands = row.split(" -> ")[1].split(", ")
            for cand in cands:
                if cand in accs:
                    accs.remove(cand)
    root = list(accs)[0]
    print("Part A:", root)

    def getsum(node, children, weights):
        if node in children:
            return weights[node] + sum(
                [getsum(child, children, weights) for child in children[node]]
            )
        else:
            return weights[node]

    # Note: This will probably not work if there is error with e.g. 2 children as legs
    def finderror(node, children, weights):
        sums = [getsum(child, children, weights) for child in children[node]]

        allequal = len(set(sums)) == 1
        if not allequal:
            countmap = {x: sums.count(x) for x in sums}
            uniquesum = min(countmap, key=lambda x: countmap[x])
            return [
                children[node][sums.index(uniquesum)],
                uniquesum - [x for x in countmap if not x == uniquesum][0],
            ]
        else:
            return [None, None]

    nextwrongnode = root
    nextwrongsum = None
    while True:
        prevwrongnode = nextwrongnode
        prevwrongsum = nextwrongsum
        nextwrongnode, nextwrongsum = finderror(prevwrongnode, children, weights)
        if nextwrongnode == None:
            break

    print("Part B:", weights[prevwrongnode] - prevwrongsum)
