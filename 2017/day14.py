import functools


def getkh(data):
    def reverse(nums, currpos, reverselength):
        numcopy = nums.copy()

        temp = []
        for j in range(reverselength):
            temp.append(nums[(currpos + j) % len(nums)])
        for j in range(reverselength):
            nums[(currpos + reverselength - 1 - j) % len(nums)] = temp[j]
        return nums

    def runalgo(data, iterations):
        nums = list(range(256))
        currpos = 0
        skipsize = 0
        for k in range(iterations):
            for step in data:
                nums = reverse(nums, currpos, step)
                currpos += step + skipsize
                skipsize += 1
        return nums

    seqend = [17, 31, 73, 47, 23]
    asci = [(ord(x)) for x in data] + seqend

    sparsehash = runalgo(asci, 64)

    densehash = [
        functools.reduce(lambda x, y: x ^ y, sparsehash[i * 16 : i * 16 + 16])
        for i in range(16)
    ]

    knothash = "".join(
        list(
            map(
                lambda x: x if len(x) == 2 else "0" + x,
                [hex(c).replace("0x", "") for c in densehash],
            )
        )
    )
    return knothash


def hextobin(x):
    scale = 16
    num_of_bits = 4
    return bin(int(x, scale))[2:].zfill(num_of_bits)


if __name__ == "__main__":
    f = open("day14.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    grid = [data + "-" + str(x) for x in range(128)]

    gridhashes = [getkh(x) for x in grid]
    binhashes = ["".join([hextobin(y) for y in x]) for x in gridhashes]

    print("Part A:", sum([sum([1 for x in y if x == "1"]) for y in binhashes]))

    # Part B
    def getneighbs(y, x, binhashes, explored):
        ranges = [-1, 0, 1]
        neighbs = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        neighbsout = []
        for nib in neighbs:
            yn = nib[0]
            xn = nib[1]
            if not (0 <= yn < len(binhashes) and 0 <= xn < len(binhashes)) or (
                (yn, xn) in explored
            ):
                continue
            if binhashes[yn][xn] == "1":
                neighbsout.append((yn, xn))
        return neighbsout

    def exploreregion(y, x, binhashes, explored):
        activeneighbs = getneighbs(y, x, binhashes, explored)
        explored.add((y, x))

        for nib in activeneighbs:
            newexp = exploreregion(nib[0], nib[1], binhashes, explored)
            explored = newexp.union(explored)
        return explored

    regions = 0
    explored = set()
    for y in range(128):
        for x in range(128):
            if (y, x) in explored:
                continue
            if binhashes[y][x] == "1":
                regions += 1
                explored = exploreregion(y, x, binhashes, explored)
    print("Part B:", regions)
