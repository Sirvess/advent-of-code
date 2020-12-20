from copy import deepcopy


def getNeighbours3d(i, j, k, previtboard):
    ran = [-1, 0, 1]
    count = 0
    for u in ran:
        for v in ran:
            for w in ran:
                if u == v == w == 0:
                    continue
                if previtboard[i - u][j - v][k - w] == "#":
                    count += 1
    return count


def getNeighbours4d(i, j, k, l, previtboard):
    ran = [-1, 0, 1]
    count = 0
    for u in ran:
        for v in ran:
            for w in ran:
                for x in ran:
                    if u == v == w == x == 0:
                        continue
                    if previtboard[i - u][j - v][k - w][l - x] == "#":
                        count += 1
    return count


def countactive3d(board):
    activecount = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            for k in range(0, len(board[i][j])):
                if board[i][j][k] == "#":
                    activecount += 1
    return activecount


def countactive4d(board):
    activecount = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            for k in range(0, len(board[i][j])):
                for l in range(0, len(board[i][j][k])):
                    if board[i][j][k][l] == "#":
                        activecount += 1
    return activecount


def runIterations3d(data, maxIter):
    boardSize = 3 * maxIter + len(data)

    xcoords = ["" for i in range(0, boardSize)]
    ycoords = [deepcopy(xcoords) for i in range(0, boardSize)]
    zcoords = [deepcopy(ycoords) for i in range(0, boardSize)]

    startIndex = maxIter
    endIndex = startIndex + len(data)

    # Initiate Board
    for j in range(startIndex, startIndex + len(data)):
        for k in range(startIndex, startIndex + len(data)):
            zcoords[startIndex][j][k] = data[0 + j - startIndex][0 + k - startIndex]

    # Iterate board
    previtboard = deepcopy(zcoords)
    for ite in range(1, maxIter + 1):
        currboard = deepcopy(previtboard)
        for i in range(startIndex - ite, startIndex + ite + 1):
            for j in range(startIndex - ite, endIndex + ite):
                for k in range(startIndex - ite, endIndex + ite):
                    cnt = getNeighbours3d(i, j, k, deepcopy(previtboard))
                    if previtboard[i][j][k] == "#":
                        if cnt == 2 or cnt == 3:
                            currboard[i][j][k] = "#"
                        else:
                            currboard[i][j][k] = "."
                    else:
                        if cnt == 3:
                            currboard[i][j][k] = "#"
                        else:
                            currboard[i][j][k] = "."
        previtboard = deepcopy(currboard)
    return previtboard


def runIterations4d(data, maxIter):
    boardSize = 3 * maxIter + len(data)

    xcoords = ["" for i in range(0, boardSize)]
    ycoords = [deepcopy(xcoords) for i in range(0, boardSize)]
    zcoords = [deepcopy(ycoords) for i in range(0, boardSize)]
    wcoords = [deepcopy(zcoords) for i in range(0, boardSize)]

    startIndex = maxIter
    endIndex = startIndex + len(data)

    # Initiate Board
    for j in range(startIndex, startIndex + len(data)):
        for k in range(startIndex, startIndex + len(data)):
            wcoords[startIndex][j][k][startIndex] = data[0 + j - startIndex][
                0 + k - startIndex
            ]

    # Iterate board
    previtboard = deepcopy(wcoords)
    for ite in range(1, maxIter + 1):
        currboard = deepcopy(previtboard)
        for i in range(startIndex - ite, startIndex + ite + 1):
            for j in range(startIndex - ite, endIndex + ite):
                for k in range(startIndex - ite, endIndex + ite):
                    for l in range(startIndex - ite, startIndex + ite + 1):
                        cnt = getNeighbours4d(i, j, k, l, deepcopy(previtboard))
                        if previtboard[i][j][k][l] == "#":
                            if cnt == 2 or cnt == 3:
                                currboard[i][j][k][l] = "#"
                            else:
                                currboard[i][j][k][l] = "."
                        else:
                            if cnt == 3:
                                currboard[i][j][k][l] = "#"
                            else:
                                currboard[i][j][k][l] = "."
        previtboard = deepcopy(currboard)

    return previtboard


if __name__ == "__main__":
    f = open("day17Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    board = runIterations3d(data, 6)
    print("Count 3dim:", countactive3d(board))

    board = runIterations4d(data, 6)
    print("Count 4dim:", countactive4d(board))
