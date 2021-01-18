def genrows(genlength, data):
    j = 0
    rows = [data]
    while j < genlength - 1:
        prevrow = rows[j]
        currrow = ""
        for i, x in enumerate(range(len(prevrow))):
            if i == 0:
                if prevrow[i + 1] == "^":
                    currrow += "^"
                else:
                    currrow += "."

            elif i == len(prevrow) - 1:
                if prevrow[i - 1] == "^":
                    currrow += "^"
                else:
                    currrow += "."
            else:
                above = prevrow[i - 1 : i + 2]
                cands = ["^^.", ".^^", "..^", "^.."]
                if above in cands:
                    currrow += "^"
                else:
                    currrow += "."
        rows.append(currrow)
        j += 1
    return rows


if __name__ == "__main__":
    f = open("day18.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    rows = genrows(40, data)
    numtiles = [[1 for c in row if c == "."] for row in rows]
    print("Part A:", sum([sum(tile) for tile in numtiles]))

    rows = genrows(400000, data)
    numtiles = [[1 for c in row if c == "."] for row in rows]
    print("Part B:", sum([sum(tile) for tile in numtiles]))
