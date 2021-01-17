def dragoncurvegen(disklength, indata):
    currdisk = data
    while len(currdisk) < disklength:
        datacopy = currdisk
        currdiskreverse = datacopy[::-1]
        currdiskreplaced = (
            currdiskreverse.replace("1", "2").replace("0", "1").replace("2", "0")
        )
        currdisk = currdisk + "0" + currdiskreplaced

    return currdisk[0:disklength]


def calcchecksum(indata):
    checksum = indata
    while True:
        if len(checksum) % 2 == 1:
            return checksum
        newsum = ""
        i = 0
        while i < len(checksum):
            if checksum[i] == checksum[i + 1]:
                newsum += "1"
            else:
                newsum += "0"
            i += 2
        checksum = newsum


if __name__ == "__main__":
    f = open("day16.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    print("Part A:", calcchecksum(dragoncurvegen(272, data)))
    print("Part B:", calcchecksum(dragoncurvegen(35651584, data)))
