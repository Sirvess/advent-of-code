def getorbitcnt(node, dep, planets):
    if not node in planets:
        return dep
    else:
        return dep + sum([getorbitcnt(x, dep + 1, planets) for x in planets[node]])


def pathtonode(node, target, path, planets):
    if node == target:
        return path + [node]
    else:
        if not node in planets:
            return None
        else:
            for x in planets[node]:
                currp = pathtonode(x, target, path + [node], planets)
                if not currp == None:
                    return currp


if __name__ == "__main__":
    f = open("day6.in", "r")
    data = [x.split(")") for x in f.read().splitlines()]
    f.close()

    planetswithorbit = set({x[0] for x in data})
    orbitingplanets = set({x[1] for x in data})
    root = list(planetswithorbit.difference(orbitingplanets)).pop()

    planets = {}
    for c in data:
        l, r = c
        if not l in planets:
            planets[l] = []
        planets[l].append(r)

    print("Part A:", getorbitcnt(root, 0, planets))

    pathtosan = pathtonode(root, "SAN", [], planets)
    pathtoyou = pathtonode(root, "YOU", [], planets)

    pathtoyou.reverse()
    pathtosan.reverse()

    for i, x in enumerate(pathtoyou):
        if x in pathtosan:
            print("Part B:", (i - 1) + (pathtosan.index(x) - 1))
            break
