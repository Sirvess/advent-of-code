def binToDec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return int(decimal)


def decToBinArr(dec):
    return bin(dec)[2:].replace("", ",").split(",")[1:-1]


def maskFilter(inp, mask, mode):
    filteredInp = mask.copy()
    for i in range(0, len(filteredInp)):
        if mode == "A":
            if i in range(0, len(inp)):
                if filteredInp[len(filteredInp) - 1 - i] == "X":
                    filteredInp[len(filteredInp) - 1 - i] = inp[len(inp) - 1 - i]
            else:
                if filteredInp[len(filteredInp) - 1 - i] == "X":
                    filteredInp[len(filteredInp) - 1 - i] = "0"
        elif mode == "B":
            if i in range(0, len(inp)):
                if filteredInp[len(filteredInp) - 1 - i] == "0":
                    filteredInp[len(filteredInp) - 1 - i] = inp[len(inp) - 1 - i]
    return filteredInp


def addToMemoryA(decaddr, decval, mask, memory):
    bitval = decToBinArr(decval)

    if decaddr in memory:
        bitval = maskFilter(memory[decaddr], bitval, "A")

    memory[decaddr] = maskFilter(bitval, mask, "A")


def addToMemoryB(decaddr, decval, mask, memory):
    def findAllAddrs(maskedaddr):
        def getOptions(bit, addr):
            cand1 = addr.copy()
            cand1[bit] = "0"
            cand2 = addr.copy()
            cand2[bit] = "1"
            return cand1, cand2

        candbits, returnarr = [], []
        for i, x in enumerate(maskedaddr):
            if x == "X":
                candbits.append(i)

        while len(candbits) > 0:
            nextbit = candbits.pop()
            if len(returnarr) == 0:
                cand1, cand2 = getOptions(nextbit, maskedaddr)
                returnarr.append(cand1)
                returnarr.append(cand2)
            else:
                newReturnArr = []
                for decaddr in returnarr:
                    cand1, cand2 = getOptions(nextbit, decaddr)
                    newReturnArr.append(cand1)
                    newReturnArr.append(cand2)
                    returnarr = newReturnArr
        return returnarr

    for item in findAllAddrs(maskFilter(decToBinArr(decaddr), mask, "B")):
        memory[binToDec(int("".join(item)))] = decval


if __name__ == "__main__":
    f = open("day14Input.txt", "r")
    data = [i.split(" = ") for i in f.read().splitlines()]

    f.close()

    currmask, memA, memB = [], {}, {}
    for row in data:
        if row[0] == "mask":
            mask = row[1]
            currmask = mask.replace("", " ").split(" ")[1:-1]
        else:
            decaddr = int(row[0][4:-1])
            decval = int(row[1])
            addToMemoryA(decaddr, decval, currmask, memA)
            addToMemoryB(decaddr, decval, currmask, memB)

    print("Part A:", sum([binToDec(int("".join(memA[i]))) for i in memA]))
    print("Part B:", sum([memB[i] for i in memB]))
