if __name__ == "__main__":
    f = open("day11.in", "r")
    data = f.read().splitlines()[0].split(",")
    f.close()
    stepsaway = set()
    pos = [0, 0]
    for act in data:
        if act == "n":
            pos[1] += 2
        elif act == "ne":
            pos[1] += 1
            pos[0] += 1
        elif act == "nw":
            pos[1] += 1
            pos[0] -= 1
        elif act == "sw":
            pos[1] -= 1
            pos[0] -= 1
        elif act == "se":
            pos[1] -= 1
            pos[0] += 1
        elif act == "s":
            pos[1] -= 2
        minnum, maxnum = map(lambda fn: fn([abs(x) for x in pos]), [min, max])
        currsteps = minnum + (maxnum - minnum) // 2
        stepsaway.add(currsteps)

    print("Part A", currsteps)
    print("Part B", max(stepsaway))
