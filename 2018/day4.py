if __name__ == "__main__":
    f = open("day4.in", "r")
    data = [row[1:].split("]") for row in f.read().splitlines()]
    data = [[row[0].split(), row[1].strip().split()] for row in data]
    f.close()

    # Sort based on date and time
    data = sorted(data, key=lambda row: (row[0][0], row[0][1]))

    guards = {}
    for x in data:
        date = x[0]
        info = x[1]

        if info[0] == "Guard":
            currguard = info[1]
            if currguard not in guards:
                guards[currguard] = [0 for i in range(60)]
        elif info[0] == "wakes":
            nowmin = int(date[1].split(":")[-1])
            prevmin = int(prevtime.split(":")[-1])
            for i in range(prevmin, nowmin):
                guards[currguard][i] += 1
        prevtime = date[1]

    guardssum = {guard: sum(guards[guard]) for guard in guards}

    maxguard = max(guardssum, key=lambda g: guardssum[g])
    maxminute = guards[maxguard].index(max(guards[maxguard]))
    print("Part A:", int(maxguard[1:]) * maxminute)

    # Type (id, maxminutes, indexOfMinute)
    gmax = max(
        [
            (guard, max(guards[guard]), guards[guard].index(max(guards[guard])))
            for guard in guards
        ],
        key=lambda x: x[1],
    )

    print("Part B:", int(gmax[0][1:]) * gmax[2])
