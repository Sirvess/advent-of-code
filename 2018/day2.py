from functools import reduce

if __name__ == "__main__":
    f = open("day2.in", "r")
    data = f.read().splitlines()
    f.close()

    twocnt = 0
    threecnt = 0
    for x in data:
        letters = {c: 0 for c in x}
        for c in x:
            letters[c] += 1

        counts = {letters[c] for c in letters}

        if 2 in counts:
            twocnt += 1
        if 3 in counts:
            threecnt += 1

    print("Part A:", twocnt * threecnt)

    for i, x in enumerate(data):
        for j, y in enumerate(data[i + 1 :]):
            diffcount = reduce(lambda a, c: a if c[0] == c[1] else a + 1, zip(x, y), 0)

            if diffcount == 1:
                eq = reduce(
                    lambda a, c: a + c[0] if c[0] == c[1] else a,
                    zip(x, y),
                    "",
                )
                print("Part B:", eq)
                break
