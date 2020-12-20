import math
import functools


def findandreplaceseamonster(i, j, board):
    seamonsterpos = [
        [0, 0],
        [1, 1],
        [1, 4],
        [0, 5],
        [0, 6],
        [1, 7],
        [1, 10],
        [0, 11],
        [0, 12],
        [1, 13],
        [1, 16],
        [0, 17],
        [-1, 18],
        [0, 18],
        [0, 19],
    ]

    def hasseamonster(i, j, board):
        for coord in seamonsterpos:
            if not board[i + coord[0]][j + coord[1]] == "#":
                return False
        return True

    if hasseamonster(i, j, board):
        for coord in seamonsterpos:
            board[i + coord[0]][j + coord[1]] = 0


def fitleft(leftsquare, newsquare):
    def fitsleft(leftsquare, rightsquare):
        for i in range(0, len(leftsquare)):
            if not leftsquare[i][len(leftsquare) - 1] == rightsquare[i][0]:
                return False
        return True

    returnsquare = newsquare.copy()
    while not fitsleft(leftsquare, returnsquare):
        returnsquare = rotate90(returnsquare)
        if not fitsleft(leftsquare, returnsquare):
            returnsquare = flipX(returnsquare)
        if not fitsleft(leftsquare, returnsquare):
            returnsquare = flipX(returnsquare)
    return returnsquare


def fittop(topsquare, newsquare):
    def fitstop(topsquare, bottomsquare):
        for i in range(0, len(topsquare)):
            if not topsquare[len(topsquare) - 1][i] == bottomsquare[0][i]:
                return False
        return True

    returnsquare = newsquare.copy()
    while not fitstop(topsquare, returnsquare):
        returnsquare = rotate90(returnsquare)
        if not fitstop(topsquare, returnsquare):
            returnsquare = flipX(returnsquare)
        if not fitstop(topsquare, returnsquare):
            returnsquare = flipX(returnsquare)
    return returnsquare


def flipX(square):
    newsquare = [[0 for i in range(0, len(square))] for i in range(0, len(square))]
    for x in range(0, len(square)):
        for y in range(0, len(square)):
            newsquare[y][x] = square[y][len(square) - 1 - x]
    return newsquare.copy()


def rotate90(square):
    newsquare = [[0 for i in range(0, len(square))] for i in range(0, len(square))]
    for x in range(0, len(square)):
        newrow = []
        for y in range(0, len(square)):
            newrow.insert(0, square[y][x])
        newsquare[x] = newrow.copy()
    return newsquare.copy()


def allrotsandflips(square):
    rots = [90, 180, 270]
    cands = [square.copy()]
    prevsquare = square.copy()
    for rot in rots:
        prevsquare = rotate90(prevsquare.copy())
        cands.append(prevsquare)

    flippedcands = [flipX(cand) for cand in cands]

    return cands + flippedcands


def getborders(square):
    return [cand[0] for cand in allrotsandflips(square)]


def ismatchingborder(border, square):
    rotatedsquares = allrotsandflips(square)
    for cand in rotatedsquares:
        if cand[0] == border:
            return True
    return False


if __name__ == "__main__":
    f = open("day20Input.txt", "r")
    squares = {
        int(y[0][5:-1]): y[1:]
        for y in [x.splitlines() for x in f.read().strip().split("\n\n")]
    }
    f.close()

    for square in squares:
        for i, row in enumerate(squares[square]):
            squares[square][i] = [x for x in row]

    borderlength = int(math.sqrt(len(squares)))

    cornersquares = set()
    bordersquares = set()
    innersquares = set()

    squareneighbours = {}

    for square in squares:
        borders = getborders(squares[square])
        matchingbordercount = 0
        squareneighbs = set()
        for border in borders:
            for candsquare in squares:
                if square == candsquare:
                    continue
                if ismatchingborder(border, squares[candsquare]):
                    matchingbordercount += 1
                    squareneighbs.add(candsquare)
                    break
        squareneighbours[square] = squareneighbs
        if matchingbordercount == 4:
            cornersquares.add(square)
        elif matchingbordercount == 6:
            bordersquares.add(square)
        else:
            innersquares.add(square)

    print(
        "Part A:",
        functools.reduce(lambda a, b: a * b, cornersquares, 1),
    )

    # Part B - calc roughness

    # Start by placing all tiles in correct position
    row = [i for i in range(0, borderlength)]
    imageid = [row.copy() for i in range(0, borderlength)]

    remcorners = list(cornersquares)
    remborders = list(bordersquares)
    reminners = list(innersquares)

    firstsquare = remcorners.pop()
    imageid[0][0] = firstsquare
    firstnbs = list(squareneighbours[firstsquare])
    imageid[0][1] = firstnbs.pop()
    remborders.remove(imageid[0][1])

    # Get top border set in imageid list
    for j in range(2, borderlength):
        cand = [
            nb
            for nb in squareneighbours[imageid[0][j - 1]]
            if not nb in imageid[0] and (nb in remborders or nb in remcorners)
        ][0]

        if cand in remborders:
            remborders.remove(cand)
            imageid[0][j] = cand
        elif cand in remcorners:
            remcorners.remove(cand)
            imageid[0][j] = cand

    # Find correct position for all tiles
    for i in range(1, borderlength):
        for j in range(0, borderlength):
            if j == 0:
                cand = [
                    cand
                    for cand in squareneighbours[imageid[i - 1][j]]
                    if cand in remborders or cand in remcorners
                ][0]
                if cand in remborders:
                    remborders.remove(cand)
                    imageid[i][j] = cand
                elif cand in remcorners:
                    remcorners.remove(cand)
                    imageid[i][j] = cand

            elif j == borderlength - 1:
                candleft = squareneighbours[imageid[i][j - 1]]
                candtop = squareneighbours[imageid[i - 1][j]]
                cand = [
                    cand
                    for cand in candtop.union(candleft)
                    if cand in candtop
                    and cand in candleft
                    and (cand in remborders or cand in remcorners)
                ][0]
                if cand in remborders:
                    remborders.remove(cand)
                    imageid[i][j] = cand
                elif cand in remcorners:
                    remcorners.remove(cand)
                    imageid[i][j] = cand
                # Border or corner
            elif i == borderlength - 1:
                if j == 0:
                    cand = [
                        cand
                        for cand in squareneighbours[imageid[i - 1][j]]
                        if cand in remcorners
                    ][0]
                    remcorners.remove(cand)
                    image[i][j] = cand
                else:
                    candleft = squareneighbours[imageid[i][j - 1]]
                    candtop = squareneighbours[imageid[i - 1][j]]
                    truecands = []
                    cand = [
                        cand
                        for cand in candtop.union(candleft)
                        if cand in candtop
                        and cand in candleft
                        and (cand in remborders or cand in remcorners)
                    ][0]
                    if cand in remborders:
                        remborders.remove(cand)
                        imageid[i][j] = cand
                    elif cand in remcorners:
                        remcorners.remove(cand)
                        imageid[i][j] = cand
                # Bottom border
            else:
                candleft = squareneighbours[imageid[i][j - 1]]
                candtop = squareneighbours[imageid[i - 1][j]]
                cand = [
                    cand
                    for cand in candtop.union(candleft)
                    if cand in candtop and cand in candleft and cand in reminners
                ][0]
                reminners.remove(cand)
                imageid[i][j] = cand

    # Now we need to replace and rotate so that borders match

    row = [i for i in range(0, borderlength)]
    imagearr = [row.copy() for i in range(0, borderlength)]

    # HACK: initial position found by hand
    imagearr[0][0] = rotate90(squares[imageid[0][0]])

    # Now replace indeces with image and rotate until fits
    for i in range(0, borderlength):
        for j in range(0, borderlength):
            if i == j == 0:
                continue
            else:
                imagearr[i][j] = squares[imageid[i][j]]
                if i == 0:
                    imagearr[i][j] = fitleft(imagearr[i][j - 1], imagearr[i][j])
                else:
                    imagearr[i][j] = fittop(imagearr[i - 1][j], imagearr[i][j])

    # Remove all borders for all tiles
    imagearrnoborder = [[] for i in range(0, borderlength)]
    for i, row in enumerate(imagearr):
        for image in row:
            imagearrnoborder[i].append([x[1:-1] for x in image[1:-1]])

    # Now merge all rows and columns to finalimg
    finalimg = []
    for row in imagearrnoborder:
        newrows = [[] for i in range(0, len(row[0]))]
        for item in row:
            for i in range(0, len(row[0])):
                newrows[i] = newrows[i] + item[i]
        for i in range(0, len(newrows)):
            finalimg.append(newrows[i])

    # Look for seamonster
    # HACK: initial position found by hand
    finalimg = flipX(rotate90(rotate90(finalimg)))
    for i in range(1, len(finalimg) - 1):
        for j in range(0, len(finalimg) - 20):
            findandreplaceseamonster(i, j, finalimg)

    # Calc roughness
    cnt = 0
    for row in finalimg:
        for c in row:
            if c == "#":
                cnt += 1
    print("Part B:", cnt)
