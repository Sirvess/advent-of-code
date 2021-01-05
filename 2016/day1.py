if __name__ == "__main__":
    f = open("day1.in", "r")
    data = f.read().splitlines()[0].split(", ")
    f.close()

    leftbearings = {"N": "W", "E": "N", "S": "E", "W": "S"}
    rightbearings = {"N": "E", "W": "N", "S": "W", "E": "S"}
    pos = [0, 0]
    bearing = "N"
    visited = {}
    revisited = []

    for coord in data:
        rot = coord[0]
        steps = int(coord[1:])

        if rot == "L":
            bearing = leftbearings[bearing]
        elif rot == "R":
            bearing = rightbearings[bearing]

        for i in range(steps):
            if pos[1] in visited:
                if pos[0] in visited[pos[1]]:
                    revisited.append(pos.copy())
                else:
                    visited[pos[1]][pos[0]] = 1
            else:
                visited[pos[1]] = {}
                visited[pos[1]][pos[0]] = 1

            if bearing == "N":
                pos[1] += 1
            elif bearing == "S":
                pos[1] -= 1
            elif bearing == "W":
                pos[0] -= 1
            elif bearing == "E":
                pos[0] += 1

    print("Part A", sum([abs(x) for x in pos]))
    print("Part B", sum([abs(x) for x in revisited[0]]))
