import functools

if __name__ == "__main__":
    f = open("day10.in", "r")
    data = [int(x) for x in f.read().split()[0].split(",")]
    f.close()

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

    parta = runalgo(data, 1)
    print("Part A:", parta[0] * parta[1])

    f = open("day10.in", "r")
    data = f.read().split()[0]
    f.close()
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

    print("Part B:", knothash)
