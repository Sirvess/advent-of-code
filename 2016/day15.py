def findvalidstarttime(initialsearch, data):
    starttime = initialsearch
    while True:
        validslot = True
        for i, capsule in enumerate(data):
            length = int(capsule[3])
            startpos = int(capsule[-1])
            outpos = (startpos + starttime + i + 1) % length
            if not outpos == 0:
                validslot = False
        if validslot == True:
            return starttime
        starttime += 1


if __name__ == "__main__":
    f = open("day15.in", "r")
    data = [row.replace(".", "").split(" ") for row in f.read().splitlines()]
    f.close()

    partaindex = findvalidstarttime(0, data)
    print("Part A:", partaindex)
    data += [["x", "x", "x", "11", "0"]]
    print("Part B:", findvalidstarttime(partaindex, data))
