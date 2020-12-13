import math


def minWait(timestamps, myId):
    minWait = math.inf
    minWaitBusId = 0
    for timestamp in timestamps:
        minTime = timestamp - (myId % timestamp)
        if minTime < minWait:
            minWait = minTime
            minWaitBusId = timestamp
    return minWait * minWaitBusId


def lcmCustom(a, b):
    return abs(a * b) // math.gcd(a, b)


if __name__ == "__main__":
    f = open("day13Input.txt", "r")
    data = f.read().splitlines()
    f.close()

    myId = int(data[0])
    timestamps = [int(i) for i in data[1].split(",") if not i == "x"]

    print("Part A: ", minWait(timestamps, myId))

    dataB = [
        {"n": int(x), "rem": i}
        for i, x in enumerate(data[1].split(","))
        if not x == "x"
    ]

    incr = dataB[0]["n"]
    firstpos = 0
    lcm = incr
    for item in dataB[1:]:
        while (firstpos + item["rem"]) % item["n"] != 0:
            firstpos += incr
        incr = lcmCustom(incr, item["n"])
    print("Part B: ", firstpos)
