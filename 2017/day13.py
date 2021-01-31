if __name__ == "__main__":
    f = open("day13.in", "r")
    data = [x.split(": ") for x in f.read().splitlines()]
    f.close()

    depths = {int(x[0]): int(x[1]) for x in data}

    def passthroughscanner(scannerdelay, permitcaught, depths):
        picoseconds = -1
        severity = 0
        while picoseconds < max(depths):
            picoseconds += 1
            if picoseconds in depths:
                previt = picoseconds + scannerdelay
                currdepth = previt % (2 * (depths[picoseconds] - 1))
                if currdepth > depths[picoseconds]:
                    currdepth = depths[picoseconds] - previt
                if currdepth == 0:
                    if permitcaught:
                        severity += picoseconds * depths[picoseconds]
                    else:
                        return "Break"

        return severity

    print("Part A:", passthroughscanner(0, True, depths))

    scannerdelay = 0
    while True:
        if not passthroughscanner(scannerdelay, False, depths) == "Break":
            print("Part B:", scannerdelay)
            break
        scannerdelay += 1
