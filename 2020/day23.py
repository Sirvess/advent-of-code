def playgame(startpos, maxmoves, maxnum=9):
    iterations = 0

    cups = startpos.copy()
    for i in range(10, maxnum + 1):
        cups.append(i)
    rightof = {x: cups[i + 1] for i, x in enumerate(cups) if i + 1 < len(cups)}
    rightof[cups[-1]] = cups[0]

    currptr = cups[0]

    while iterations < maxmoves:
        currcups = []
        nxt = rightof[currptr]
        for j in range(3):
            currcups.append(nxt)
            nxt = rightof[nxt]
        rightof[currptr] = nxt
        destptr = currptr - 1
        while destptr in currcups or destptr < 1:
            destptr -= 1
            if destptr < 1:
                destptr = maxnum
        newnext = rightof[destptr]
        rightof[destptr] = currcups[0]
        rightof[currcups[-1]] = newnext

        currptr = rightof[currptr]
        iterations += 1
    return rightof


if __name__ == "__main__":
    startpos = [8, 5, 3, 1, 9, 2, 6, 4, 7]

    parta = playgame(startpos.copy(), 100)
    astring = ""
    pos = 1
    while not parta[pos] == 1:
        astring += str(parta[pos])
        pos = parta[pos]
    print("Part A:", astring)

    partb = playgame(startpos.copy(), 10000000, 1000000)
    print("Part B:", partb[1] * partb[partb[1]])
