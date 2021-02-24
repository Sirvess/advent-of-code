def getplants(generations, initstate, patterns):
    prevgen = [".", ".", ".", ".", "."] + list(initstate)
    leftpadding = 5

    prevsum = sum([i - leftpadding for i, x in enumerate(prevgen) if x == "#"])
    consecutivesums, previncrement = 0, 0
    for i in range(generations):
        currgen = ["." for i in prevgen]
        if not prevgen[-5:] == ["." for z in range(5)]:
            currgen = currgen + ["." for z in range(5)]

        for row in patterns:
            pattern, patterngoal = row
            for k, c in enumerate(prevgen[:-4]):
                match = True
                for l in range(len(pattern)):
                    if not prevgen[k + l] == pattern[l]:
                        match = False
                        break
                if match == True:
                    currgen[k + 2] = patterngoal
        while currgen[:5] == ["." for z in range(5)]:
            currgen = currgen[1:]
            leftpadding -= 1

        prevgen = currgen
        currsum = sum([i - leftpadding for i, x in enumerate(prevgen) if x == "#"])
        currincrement = currsum - prevsum
        prevsum = currsum

        if currincrement == previncrement:
            consecutivesums += 1
        else:
            consecutivesums = 0
        previncrement = currincrement

        # Assume that with high generations, growth rate will stabilize and be constant
        if consecutivesums == 3:
            return sum([i - leftpadding for i, x in enumerate(prevgen) if x == "#"]) + (
                generations - i - 1
            ) * (currincrement)

    return sum([i - leftpadding for i, x in enumerate(prevgen) if x == "#"])


if __name__ == "__main__":
    f = open("day12.in", "r")
    data = f.read().splitlines()
    f.close()

    initstate = str(data[0].split(":")[-1].strip())
    patterns = [x.split(" => ") for x in data[2:]]

    print("Part A:", getplants(20, initstate, patterns))
    print("Part B:", getplants(50000000000, initstate, patterns))
