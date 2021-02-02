if __name__ == "__main__":
    f = open("day15.in", "r")
    data = f.read().splitlines()
    f.close()

    def getnextnum(prevnum, factor, divisor):
        newnum = (prevnum * factor) % 2147483647
        while not newnum % divisor == 0:
            newnum = (newnum * factor) % 2147483647
        return newnum

    def getmatchcount(iterations, a, b, diva, divb):
        preva = a
        prevb = b
        factora = 16807
        factorb = 48271
        matchcount = 0
        for i in range(iterations):
            preva = getnextnum(preva, factora, diva)
            prevb = getnextnum(prevb, factorb, divb)
            newa, newb = [bin(x)[-16:] for x in [preva, prevb]]
            if newa == newb:
                matchcount += 1
        return matchcount

    astart, bstart = [int(x.split()[-1]) for x in data]
    print("Part A:", getmatchcount(40000000, astart, bstart, 1, 1))
    print("Part B:", getmatchcount(5000000, astart, bstart, 4, 8))
