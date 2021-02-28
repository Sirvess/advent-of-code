def getfuel(x):
    return x // 3 - 2


def reducefuel(x):
    fuelsum = 0
    prevfuel = x
    while getfuel(prevfuel) >= 0:
        prevfuel = getfuel(prevfuel)
        fuelsum += prevfuel
    return fuelsum


if __name__ == "__main__":
    f = open("day1.in", "r")
    data = [int(x) for x in f.read().splitlines()]
    f.close()

    print("Part A:", sum(map(getfuel, data)))
    print("Part B:", sum(map(reducefuel, data)))
