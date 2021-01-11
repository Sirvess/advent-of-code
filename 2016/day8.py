if __name__ == "__main__":
    f = open("day8.in", "r")
    data = [row.replace("by ", "").split(" ") for row in f.read().splitlines()]
    f.close()

    width = 50
    height = 6
    row = ["." for i in range(width)]
    screen = [row.copy() for i in range(height)]

    for item in data:
        action = item[0]
        if action == "rect":
            data = item[1].split("x")
            rectwidth = int(data[0])
            rectheight = int(data[1])
            for i in range(rectheight):
                for j in range(rectwidth):
                    screen[i][j] = "#"
        elif action == "rotate":
            direction = item[1]
            pos = item[2].split("=")
            startcoord = int(pos[1])
            rotvalue = int(item[3])

            if direction == "row":
                oldrow = screen[startcoord].copy()
                newrow = ["" for i in range(len(oldrow))]
                for i, x in enumerate(range(len(oldrow))):
                    nextcoord = i - rotvalue % len(oldrow)
                    newrow[i] = oldrow[nextcoord]
                screen[startcoord] = newrow

            elif direction == "column":
                oldcol = [row[startcoord] for row in screen].copy()
                newcol = ["" for i in range(len(screen))]
                for i, x in enumerate(range(len(screen))):
                    nextcoord = i - rotvalue % len(screen)
                    newcol[i] = oldcol[nextcoord]

                for i in range(len(screen)):
                    screen[i][startcoord] = newcol[i]

    turnedonlights = sum([sum([1 for x in row if x == "#"]) for row in screen])
    print("Part A:", turnedonlights)

    # Solve part B by reading the output in the terminal
    [print(row) for row in screen]
