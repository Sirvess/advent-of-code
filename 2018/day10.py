import re

if __name__ == "__main__":
    f = open("day10.in", "r")
    data = f.read().splitlines()
    data = [str(re.sub("position=<|velocity=<|,|>", "", x)).split() for x in data]
    data = [[i, (x[0], x[1]), (x[2], x[3])] for i, x in enumerate(data)]
    f.close()

    velo = {x[0]: (int(x[2][0]), int(x[2][1])) for x in data}
    prevpos = {x[0]: (int(x[1][0]), int(x[1][1])) for x in data}

    def getcoorddiff(coords):
        xcoords = [x[0] for x in coords]
        ycoords = [x[1] for x in coords]
        return max(xcoords) - min(xcoords) + max(ycoords) - min(ycoords)

    it = 0
    prevdiff = getcoorddiff([prevpos[x] for x in prevpos])
    while True:
        it += 1
        newpos = prevpos.copy()

        for i in prevpos:
            newpos[i] = (prevpos[i][0] + velo[i][0], prevpos[i][1] + velo[i][1])
        coords = set([newpos[x] for x in newpos])
        currdiff = getcoorddiff(coords)
        # Velocities constant =>
        # find inflexion point where coordinates are closest to one another to read message
        if currdiff > prevdiff:
            paintedc = [
                ["." for i in range(max([x[0] for x in coords]))]
                for i in range(max([x[1] for x in coords]))
            ]
            for x in prevpos:
                xc = prevpos[x][0]
                yc = prevpos[x][1]
                paintedc[yc][xc] = "#"
            for l in paintedc[min([x[1] for x in coords]) :]:
                print("".join(l)[min([x[0] for x in coords]) :])
            print("Part B:", it - 1)
            break
        prevpos = newpos.copy()
        prevdiff = currdiff
