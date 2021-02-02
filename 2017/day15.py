if __name__ == "__main__":
    f = open("day15.in", "r")
    data = f.read().splitlines()
    f.close()

    def getnextnum(prevnum, factor, divisor):
        newnum = (prevnum * factor) % 2147483647
        while not newnum % divisor == 0:
            newnum = (newnum * factor) % 2147483647
        return newnum

    def numgen(iterations, startnum, factor, divisor):
        i = 0
        prevnum = startnum
        while i < iterations:
            prevnum = getnextnum(prevnum, factor, divisor)
            yield bin(prevnum)[-16:]
            i += 1

    def getmatchcount(iterations, a, b, diva, divb):
        factora = 16807
        factorb = 48271
        alist = (x for x in numgen(iterations, a, factora, diva))
        blist = (x for x in numgen(iterations, b, factorb, divb))
        return sum((1 for x in zip(alist, blist) if x[0] == x[1]))

    astart, bstart = [int(x.split()[-1]) for x in data]
    print("Part A:", getmatchcount(40000000, astart, bstart, 1, 1))
    print("Part B:", getmatchcount(5000000, astart, bstart, 4, 8))
