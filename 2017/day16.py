def dance(arr, data):
    for act in data:
        if act[0] == "s":
            for i in range(int(act[1:]) % len(arr)):
                arr.insert(0, arr.pop(-1))
        else:
            items = act[1:].split("/")
            if act[0] == "p":
                ai, bi = [arr.index(x) for x in items]
                a, b = items
            elif act[0] == "x":
                ai, bi = [int(x) for x in items]
                a, b = [arr[x] for x in [ai, bi]]
            arr[ai] = b
            arr[bi] = a
    return arr


if __name__ == "__main__":
    f = open("day16.in", "r")
    data = f.read().splitlines()[0].split(",")
    f.close()

    initpos = list("abcdefghijklmnop")
    onedance = dance(initpos.copy(), data)
    print("Part A:", "".join(onedance))

    reference = "".join(onedance)

    i = 0
    loopsize = 1000000000
    nextdance = onedance.copy()
    while True:
        nextdance = dance(nextdance.copy(), data)
        i += 1
        if "".join(nextdance) == reference:
            break

    nextdance = list(reference)
    for i in range(loopsize % i - 1):
        nextdance = dance(nextdance.copy(), data)

    print("Part B:", "".join(nextdance))
