import itertools

if __name__ == "__main__":
    f = open("day9.in", "r")
    data = [x.replace(" to ", " = ").split(" = ") for x in f.read().splitlines()]
    f.close()

    paths = {}
    for x in data:
        if not x[0] in paths:
            paths[x[0]] = {}
        paths[x[0]][x[1]] = int(x[2])
        if not x[1] in paths:
            paths[x[1]] = {}
        paths[x[1]][x[0]] = int(x[2])

    nodes = set(paths)
    permutations = itertools.permutations(nodes)

    pathlengths = set()
    for permutation in permutations:
        pathlength = sum([paths[x[0]][x[1]] for x in zip(permutation, permutation[1:])])
        pathlengths.add(pathlength)
    print("Part A:", min(pathlengths))
    print("Part B:", max(pathlengths))
