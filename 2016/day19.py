if __name__ == "__main__":
    f = open("day19.in", "r")
    data = f.read().splitlines()[0]
    f.close()

    elfcount = int(data)
    i = 0

    elfPresents = {i: 1 for i in range(elfcount)}
    while elfcount > 1:
        if i == len(elfPresents):
            i = 0
        if elfPresents[i] == 0:
            i += 1
            if i == len(elfPresents):
                i = 0
            continue
        j = i + 1
        if j == len(elfPresents):
            j = 0
        while elfPresents[j] == 0:
            j += 1
            if j == len(elfPresents):
                j = 0
        elfPresents[i] += elfPresents[j]
        elfPresents[j] = 0
        i = j + 1
        elfcount -= 1

    # Starts with 0
    print("Part A:", [elf + 1 for elf in elfPresents if elfPresents[elf] > 0][0])

    elfcount = int(data)
    i = 0
    elfPresents = {i: 1 for i in range(1, elfcount + 1)}
    elvesWithPresents = [i for i in range(1, elfcount + 1)]
    while len(elvesWithPresents) > 1:
        if i >= len(elvesWithPresents):
            i = 0
        curr = elvesWithPresents[i]

        oppositeIndex = i + (len(elvesWithPresents) // 2)
        if oppositeIndex >= len(elvesWithPresents):
            i -= 1
            oppositeIndex -= len(elvesWithPresents)
        oppositeNo = elvesWithPresents[oppositeIndex]
        oppositePresents = elfPresents[oppositeNo]

        elfPresents[curr] += oppositePresents
        elfPresents[oppositeNo] = 0
        elvesWithPresents.pop(oppositeIndex)
        i += 1
    print("Part B:", elvesWithPresents[0])
