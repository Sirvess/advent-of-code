import math

if __name__ == "__main__":
    f = open("day13.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    def iswall(y, x, num):
        summa = x * x + 3 * x + 2 * x * y + y + y * y + num
        binsumma = bin(summa)
        return binsumma.count("1") % 2 == 1

    def minpath(node, currmin, visited):
        curr = node
        if curr["coord"] in visited:
            if curr["depth"] >= visited[curr["coord"]]:
                return math.inf
        else:
            visited[curr["coord"]] = curr["depth"]
        if curr["coord"] == (39, 31):
            return curr["depth"]
        elif curr["depth"] > currmin:
            return math.inf

        surrounding = [-1, 0, 1]
        neighbs = []
        for dy in surrounding:
            for dx in surrounding:
                if dy == dx or (dy == -1 and dx == 1) or (dy == 1 and dx == -1):
                    continue
                cand = (curr["coord"][0] + dy, curr["coord"][1] + dx)
                if not cand == curr["coord"] and not cand[0] < 0 and not cand[1] < 0:
                    if not iswall(cand[0], cand[1], data):
                        if not (cand[0], cand[1]) in curr["path"]:
                            neighbs.append(cand)

        for neighb in neighbs:
            newnode = {
                "coord": neighb,
                "depth": curr["depth"] + 1,
                "neighbs": [],
                "path": curr["path"] + [curr["coord"]],
            }
            curr["neighbs"].append(newnode)

        for nib in curr["neighbs"]:
            cand = minpath(nib, currmin, visited)
            if cand < currmin:
                currmin = cand
        return currmin

    print(
        "Part A:",
        minpath({"coord": (1, 1), "depth": 0, "neighbs": [], "path": []}, math.inf, {}),
    )

    def maxvisit(node, visited):
        curr = node
        if not curr["coord"] in visited:
            visited.add(curr["coord"])

        if curr["depth"] == 50:
            return visited

        surrounding = [-1, 0, 1]
        neighbs = []
        for dy in surrounding:
            for dx in surrounding:
                if dy == dx or (dy == -1 and dx == 1) or (dy == 1 and dx == -1):
                    continue
                cand = (curr["coord"][0] + dy, curr["coord"][1] + dx)
                if not cand[0] < 0 and not cand[1] < 0:
                    if not iswall(cand[0], cand[1], data):
                        if not (cand[0], cand[1]) in curr["path"]:
                            neighbs.append(cand)

        for neighb in neighbs:
            newnode = {
                "coord": neighb,
                "depth": curr["depth"] + 1,
                "neighbs": [],
                "path": curr["path"] + [curr["coord"]],
            }
            curr["neighbs"].append(newnode)

        for nib in curr["neighbs"]:
            maxvisit(nib, visited)
        return visited

    print(
        "Part B:",
        len(maxvisit({"coord": (1, 1), "depth": 0, "neighbs": [], "path": []}, set())),
    )
