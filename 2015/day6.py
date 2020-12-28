if __name__ == "__main__":
    f = open("day6.in", "r")
    data = f.read().splitlines()
    f.close()

    data = [row.split("through") for row in data]
    data = [[row[0].rstrip().split(" "), row[1].lstrip()] for row in data]
    data = [
        {
            "act": "".join(row[0][:-1]),
            "st": row[0][-1].split(","),
            "en": row[1].split(","),
        }
        for row in data
    ]

    lights = [0 for i in range(0, 1000)]
    lights = [lights.copy() for i in range(0, 1000)]

    for action in data:
        curract = action["act"]
        for i in range(int(action["st"][0]), int(action["en"][0]) + 1):
            for j in range(int(action["st"][1]), int(action["en"][1]) + 1):
                if curract == "turnon":

                    lights[i][j] = 1
                elif curract == "toggle":

                    if lights[i][j] == 0:
                        lights[i][j] = 1
                    else:
                        lights[i][j] = 0
                elif curract == "turnoff":
                    lights[i][j] = 0

    print("Part A:", sum([sum(light) for light in lights]))

    lights = [0 for i in range(0, 1000)]
    lights = [lights.copy() for i in range(0, 1000)]

    for action in data:
        curract = action["act"]
        for i in range(int(action["st"][0]), int(action["en"][0]) + 1):
            for j in range(int(action["st"][1]), int(action["en"][1]) + 1):
                if curract == "turnon":
                    lights[i][j] += 1
                elif curract == "toggle":
                    lights[i][j] += 2
                elif curract == "turnoff":
                    if lights[i][j] > 0:
                        lights[i][j] -= 1

    print("Part B:", sum([sum(light) for light in lights]))
