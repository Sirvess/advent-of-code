import math
from collections import defaultdict

# Returns number of directly visible, plus all vectors
def getvisible(inputasteroid, asteroids):
    y = inputasteroid[1]
    x = inputasteroid[0]
    grads = defaultdict(set)
    for asteroid in asteroids:
        if asteroid == inputasteroid:
            continue
        direction = (asteroid[0] - x, asteroid[1] - y)
        absv = math.sqrt(direction[0] ** 2 + direction[1] ** 2)
        v = (round(direction[0] / absv, 12), round(direction[1] / absv, 12))
        grads[v].add(asteroid)
    return len(grads), grads


if __name__ == "__main__":
    f = open("day10.in", "r")
    data = f.read().splitlines()
    f.close()

    asteroidcoords = set()
    for i, x in enumerate(data):
        for j, y in enumerate(x):
            if y == "#":
                asteroidcoords.add((j, i))

    maxvisible, bestcoord = 0, (0, 0)
    for asteroid in asteroidcoords:
        canbeseen, _ = getvisible(asteroid, asteroidcoords)
        if canbeseen > maxvisible:
            maxvisible = canbeseen
            bestcoord = asteroid
    print("Part A:", maxvisible)

    startpos = bestcoord
    _, asteroids = getvisible(startpos, asteroidcoords)

    asteroidangles = {
        math.degrees(math.atan2(v[1], v[0])): asteroids[v] for v in asteroids
    }

    sortedangles = {
        c: sorted(
            [(p[0] - startpos[0], p[1] - startpos[1]) for p in asteroidangles[c]],
            key=lambda p: math.sqrt((p[0] ** 2) + p[1] ** 2),
        )
        for c in asteroidangles
    }

    moddedangles = {(x + 90 + 360) % 360: sortedangles[x] for x in sortedangles}

    def incrementdegree(deg, rems):
        anglesnotequal = list(filter(lambda x: not x == deg, rems))
        if len(anglesnotequal) == 0:
            return deg
        else:
            outputangles = sorted(
                [
                    x if x >= 0 else x + 360
                    for x in map(lambda x: x - deg, anglesnotequal)
                ]
            )
            return outputangles[0] + deg if outputangles[0] + deg < 360 else 0

    degree = 0
    remangles = list(moddedangles)
    vaporized = []
    while len(remangles) > 0:
        tovaporize = moddedangles[degree].pop(0)
        vaporized.append((tovaporize[0] + startpos[0], tovaporize[1] + startpos[1]))
        if len(moddedangles[degree]) == 0:
            del moddedangles[degree]
            remangles = list(moddedangles)
        degree = incrementdegree(degree, remangles)

    print("Part B:", vaporized[199][0] * 100 + vaporized[199][1])
