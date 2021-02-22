if __name__ == "__main__":
    f = open("day11.in", "r")
    data = int(f.read().splitlines()[0])
    f.close()

    numcoords = 300
    serialnumber = data

    # initiate powerlevels
    powerlevels = [[0 for i in range(numcoords)] for j in range(numcoords)]
    for y, row in enumerate(powerlevels):
        for x, cell in enumerate(row):
            xcoord = x + 1
            ycoord = y + 1
            rackid = xcoord + 10
            powerlevel = (rackid * ycoord + serialnumber) * rackid
            if powerlevel < 100:
                powerlevel = 0
            else:
                powerlevel = int(str(powerlevel)[-3])
            powerlevel -= 5
            powerlevels[y][x] = powerlevel

    cache = {}

    # Kind of ugly - dependent on outer cache, requires to start from squaresize 1
    def getmaxpowerlevel(squaresize):
        maxscore = 0
        topleftcoord = (0, 0)
        for y, row in enumerate(powerlevels[0:-squaresize]):
            for x, cell in enumerate(row[0:-squaresize]):
                if not (x, y) in cache:
                    cache[(x, y)] = {0: 0}

                currsum = cache[(x, y)][squaresize - 1]
                for i in range(squaresize):
                    currsum += powerlevels[y + squaresize - 1][x + i]
                    currsum += powerlevels[y + i][x + squaresize - 1]
                currsum -= powerlevels[y + squaresize - 1][x + squaresize - 1]

                cache[(x, y)][squaresize] = currsum
                if currsum > maxscore:
                    maxscore = currsum
                    topleftcoord = (x + 1, y + 1)
        return maxscore, topleftcoord

    maxscore = 0
    coordandsize = (0, 0, 0)
    for i in range(1, 301):
        score, coord = getmaxpowerlevel(i)
        if i == 3:
            print("Part A:", coord)
        if score > maxscore:
            maxscore = score
            coordandsize = (coord[0], coord[1], i)

    print("Part B:", coordandsize)
