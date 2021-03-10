import re

if __name__ == "__main__":
    f = open("day25.in", "r")
    data = f.read().splitlines()
    f.close()

    row, col = re.findall(r"\d+", data[0])
    targetcode = (int(col), int(row))
    prevcode = (1, 1)
    codes = {prevcode: 20151125}
    direction = "d"
    prevmax = 1
    while targetcode not in codes:
        if direction == "d":
            prevmax += 1
            nextcode = (1, prevmax)
            direction = "ur"
        elif direction == "ur":
            if nextcode[1] == 1:
                direction = "d"
                continue
            nextcode = (prevcode[0] + 1, prevcode[1] - 1)
        nextcodeval = (codes[prevcode] * 252533) % 33554393
        codes[nextcode] = nextcodeval
        prevcode = nextcode

    print("Part A:", codes[targetcode])
