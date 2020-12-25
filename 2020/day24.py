if __name__ == "__main__":
    f = open("day24Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    tiles = {}
    for j, row in enumerate(data):
        pos = [0, 0]
        i = 0
        while i < len(row):
            if row[i] == "s" or row[i] == "n":
                c = "x"
                if not i == len(row) - 1:
                    if row[i + 1] == "e" or row[i + 1] == "w":
                        c = row[i] + row[i + 1]
                        i += 2
                else:
                    c = row[i]
                    i += 1
            else:
                c = row[i]
                i += 1
            if c == "e":
                pos[0] += 2
            elif c == "w":
                pos[0] -= 2
            elif c == "nw":
                pos[0] -= 1
                pos[1] -= 1
            elif c == "ne":
                pos[0] += 1
                pos[1] -= 1
            elif c == "se":
                pos[0] += 1
                pos[1] += 1
            elif c == "sw":
                pos[0] -= 1
                pos[1] += 1

        key = tuple(pos)
        if key in tiles:
            if tiles[key] == "white":
                tiles[key] = "black"
            else:
                tiles[key] = "white"
        else:
            tiles[key] = "black"
    blacktiles = {key: tiles[key] for key in tiles if tiles[key] == "black"}
    print("Part A:", sum([1 for key in blacktiles]))

    def fliptiles(blacktiles):
        blacktilesnextiter = {}
        for tile in blacktiles:
            neighbs = [
                (tile[0] + 2, tile[1]),
                (tile[0] - 2, tile[1]),
                (tile[0] - 1, tile[1] - 1),
                (tile[0] + 1, tile[1] - 1),
                (tile[0] - 1, tile[1] + 1),
                (tile[0] + 1, tile[1] + 1),
            ]
            blackcount = 0
            tocheckwhites = []
            for neighb in neighbs:
                if neighb in blacktiles:
                    blackcount += 1
                else:
                    tocheckwhites.append(neighb)

            if blackcount == 1 or blackcount == 2:
                blacktilesnextiter[tile] = "black"

            for tile in tocheckwhites:
                neighbs = [
                    (tile[0] + 2, tile[1]),
                    (tile[0] - 2, tile[1]),
                    (tile[0] - 1, tile[1] - 1),
                    (tile[0] + 1, tile[1] - 1),
                    (tile[0] - 1, tile[1] + 1),
                    (tile[0] + 1, tile[1] + 1),
                ]
                blackcount = 0
                for neighb in neighbs:
                    if neighb in blacktiles:
                        blackcount += 1
                if blackcount == 2:
                    blacktilesnextiter[tile] = "black"
        return blacktilesnextiter

    iterations = 100
    curr = blacktiles
    for i in range(iterations):
        curr = fliptiles(curr)
    print("Part B:", sum([1 for tile in curr]))
