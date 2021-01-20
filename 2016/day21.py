import itertools


def scramble(instr, data):
    currstr = instr
    for instruction in data:
        strarr = list(currstr)
        action = instruction[0]
        if action == "swap":
            z = instruction[1]
            if z == "position":
                startpos = int(instruction[2])
                endpos = int(instruction[-1])
                endchar = strarr[endpos]
                strarr[endpos] = strarr[startpos]
                strarr[startpos] = endchar
            elif z == "letter":
                startpos = strarr.index(instruction[2])
                endpos = strarr.index(instruction[-1])
                endchar = strarr[endpos]
                strarr[endpos] = strarr[startpos]
                strarr[startpos] = endchar
        elif action == "rotate":
            z = instruction[1]
            if z == "based":
                tofind = instruction[-1]
                tofindindex = strarr.index(tofind)
                amount = 1 + tofindindex
                if tofindindex >= 4:
                    amount += 1
                direction = "right"
            else:
                amount = int(instruction[2])
                direction = z
            oldarr = strarr.copy()
            for l in range(amount):
                newarr = oldarr.copy()
                for i in range(len(newarr)):
                    if direction == "left":
                        newarr[i - 1] = oldarr[i]
                    elif direction == "right":
                        newarr[i] = oldarr[i - 1]
                oldarr = newarr.copy()
            strarr = oldarr.copy()
        elif action == "move":
            fromindex = int(instruction[2])
            toindex = int(instruction[-1])
            item = strarr.pop(fromindex)
            strarr.insert(toindex, item)
        elif action == "reverse":
            fromindex = int(instruction[2])
            toindex = int(instruction[-1])
            strarr = (
                strarr[:fromindex]
                + strarr[fromindex : toindex + 1][::-1]
                + strarr[toindex + 1 :]
            )
        currstr = "".join(strarr)
    return currstr


if __name__ == "__main__":
    f = open("day21.in", "r")
    data = [row.split(" ") for row in f.read().splitlines()]
    f.close()

    currstr = "abcdefgh"
    print("Part A:", scramble(currstr, data))

    combinations = itertools.permutations(currstr)
    for comb in combinations:
        teststr = "".join(comb)
        output = scramble(teststr, data)
        if output == "fbgdceah":
            print("Part B:", teststr)
            break
