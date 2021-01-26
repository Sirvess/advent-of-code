if __name__ == "__main__":
    f = open("day6.in", "r")
    data = [[int(x) for x in row.split("\t")] for row in f.read().splitlines()][0]
    f.close()

    seen = {}
    last = data.copy()
    cycles = 0
    while tuple(last) not in seen:
        seen[tuple(last)] = cycles
        nextmax = max(last)
        maxindex = last.index(nextmax)
        last[maxindex] = 0
        for i in range(nextmax):
            index = (maxindex + 1 + i) % len(last)
            last[index] += 1
        cycles += 1

    print("Part A:", cycles)
    print("Part B:", cycles - seen[tuple(last)])
