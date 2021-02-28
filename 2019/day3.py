if __name__ == "__main__":
    f = open("day3.in", "r")
    data = [line.split(",") for line in f.read().splitlines()]
    f.close()

    coords = {}
    stepsToCoord = {}
    for lineindex, line in enumerate(data):
        coords[lineindex] = set()
        coord = (0, 0)
        totsteps = 0
        stepsToCoord[lineindex] = {}
        for instr in line:
            path = instr[0]
            steps = int(instr[1:])
            for i in range(steps):
                if path == "U":
                    coord = (coord[0], coord[1] - 1)
                elif path == "D":
                    coord = (coord[0], coord[1] + 1)
                elif path == "L":
                    coord = (coord[0] - 1, coord[1])
                elif path == "R":
                    coord = (coord[0] + 1, coord[1])
                totsteps += 1
                stepsToCoord[lineindex][coord] = totsteps
                coords[lineindex].add(coord)

    # We know there are only 2 lines
    duplicates = {i for i in coords[1] if i in coords[0]}
    print("Part A:", min([abs(x[0]) + abs(x[1]) for x in duplicates]))
    print("Part B:", min([stepsToCoord[0][x] + stepsToCoord[1][x] for x in duplicates]))
