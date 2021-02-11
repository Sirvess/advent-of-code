if __name__ == "__main__":
    f = open("day3.in", "r")
    data = [x.split() for x in f.read().splitlines()]
    f.close()

    maxsize = 1000
    squares = [[0 for i in range(maxsize)] for i in range(maxsize)]
    for x in data:
        xpos, ypos = [int(z) for z in x[2].replace(":", "").split(",")]
        xr, yr = [int(z) for z in x[3].split("x")]
        for j in range(yr):
            for i in range(xr):
                squares[j + ypos][i + xpos] += 1
    print("Part A:", sum([sum([1 for x in y if x >= 2]) for y in squares]))

    for x in data:
        xpos, ypos = [int(z) for z in x[2].replace(":", "").split(",")]
        xr, yr = [int(z) for z in x[3].split("x")]
        nonOverlap = True
        for j in range(yr):
            for i in range(xr):
                if not squares[j + ypos][i + xpos] == 1:
                    nonOverlap = False
        if nonOverlap == True:
            print("Part B:", x[0])
            break
