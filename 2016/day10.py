if __name__ == "__main__":
    f = open("day10.in", "r")
    data = [val.split(" ") for val in f.read().splitlines()]
    f.close()

    bots = {}
    for inp in [val for val in data if val[0] == "value"]:
        target = int(inp[-1])
        value = int(inp[1])
        if not target in bots:
            bots[target] = []
        bots[target].append(value)

    outputs = {}
    botswchips = [bot for bot in bots if len(bots[bot]) > 0]
    while len(botswchips) > 1:
        for inp in [val for val in data if not val[0] == "value"]:
            curr = int(inp[1])
            if curr in bots and len(bots[curr]) == 2:
                if 17 in bots[curr] and 61 in bots[curr]:
                    print("Part A:", curr)
                lowval = min(bots[curr])
                highval = max(bots[curr])
                bots[curr] = []

                lowtargetType = inp[5]
                lowtargetVal = int(inp[6])
                hightargetType = inp[10]
                hightargetVal = int(inp[-1])

                if lowtargetType == "output":
                    containingdict = outputs
                else:
                    containingdict = bots
                if not lowtargetVal in containingdict:
                    containingdict[lowtargetVal] = []
                containingdict[lowtargetVal].append(lowval)

                if hightargetType == "output":
                    containingdict = outputs
                else:
                    containingdict = bots
                if not hightargetVal in containingdict:
                    containingdict[hightargetVal] = []
                containingdict[hightargetVal].append(highval)
            botswchips = [bot for bot in bots if len(bots[bot]) > 0]

    print("Part B:", outputs[0][0] * outputs[1][0] * outputs[2][0])
