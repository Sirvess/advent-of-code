def race(raceduration, data):
    deers = {deer[0]: 0 for deer in data}
    for deer in data:
        deername = deer[0]
        flyspeed = int(deer[1])
        flyduration = int(deer[2])
        restduration = int(deer[3])

        iterationduration = flyduration + restduration
        iterationlength = flyspeed * flyduration

        iterations = raceduration // iterationduration
        fulliterationlength = iterations * iterationlength
        remsec = raceduration % iterationduration

        partialiterationlength = 0
        if remsec >= flyduration:
            partialiterationlength = flyduration * flyspeed
        else:
            partialiterationlength = remsec * flyspeed

        deerlength = fulliterationlength + partialiterationlength
        deers[deername] = deerlength

    leaderpts = max([deers[deer] for deer in deers])
    leader = [deer for deer in deers if deers[deer] == leaderpts][0]
    return leader, leaderpts


if __name__ == "__main__":
    f = open("day14.in", "r")
    data = [
        deer.replace(" can fly", "")
        .replace(" km/s for", "")
        .replace(" seconds", "")
        .replace(", but then must rest for", "")
        .replace(".", "")
        .split(" ")
        for deer in f.read().splitlines()
    ]
    f.close()

    raceduration = 2503
    winner, pts = race(raceduration, data)
    print("Part A:", pts)

    deerpts = {deer[0]: 0 for deer in data}
    for i in range(1, raceduration + 1):
        winner, pts = race(i, data)
        deerpts[winner] += 1

    print("Part B:", max([deerpts[deer] for deer in deerpts]))
